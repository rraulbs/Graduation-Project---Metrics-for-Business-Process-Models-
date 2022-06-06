#!/bin/bash
set -eo pipefail

function update_kibana() {
    if [ -f "./logs/continuous-update-enabled.txt" ];
    then
        python3 BPMN_element_counter.py /tmp/processes /tmp/csv/output.csv;
        pwsh PrepareData.ps1 -Filename "$PWD/csv/output.csv";
        sleep 15;
        echo "Sending updates..."
        curl -XPOST elasticsearch:9200/processes/_bulk -H "Content-Type: application/x-ndjson" --data-binary @"bulk.json";
        sleep 15;
        pwsh trigger.ps1 -restoreOptions;
    fi
}

function main () {
    current_date_time="`date "+%Y-%m-%d %H:%M:%S"`";
    echo $current_date_time >> $PWD/logs/redhat-static-metrics-started.txt;
    sleep 60;
    while true
    do
        if [ ! -f "./logs/redhat-static-metrics-started.txt" ] ; 
        then
            exit 0
        fi
        update_kibana;
        pwsh trigger.ps1 -startOptions;
    done
}
main "${@}"
