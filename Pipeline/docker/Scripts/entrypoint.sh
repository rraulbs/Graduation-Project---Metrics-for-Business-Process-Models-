#!/bin/bash
set -eo pipefail

function update_kibana() {
    python3 BPMN_element_counter.py /processes output.csv
    pwsh PrepareData.ps1 -Filename "output.csv";
    while true
    do
        sleep 15;
        echo "Sending updates..."
        curl -XPOST elasticsearch:9200/processes/_bulk -H "Content-Type: application/x-ndjson" --data-binary @"bulk.json";
        sleep 15;
    done
}

function main () {
    # Add here logic: Every x minutes do the following ...
    sleep 60;
    if [ ! -f "redhat-...-started.txt" ]; then
        current_date_time="`date "+%Y-%m-%d %H:%M:%S"`";
        echo $current_date_time > redhat-ubi8-started.txt;
        update_kibana;
    fi
}
main "${@}"