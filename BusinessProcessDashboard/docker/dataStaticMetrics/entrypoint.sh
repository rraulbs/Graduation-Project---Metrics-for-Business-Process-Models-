#!/bin/bash
set -eo pipefail

function update_kibana() {
    python3 BPMN_element_counter.py /tmp/processes output.csv;
    pwsh PrepareData.ps1 -Filename "output.csv";
    sleep 15;
    echo "Sending updates..."
    curl -XPUT elasticsearch:9200/processes/_bulk -H "Content-Type: application/x-ndjson" --data-binary @"bulk.json";
    sleep 15;
}

function post_kibana(){
    curl -XPOST elasticsearch:9200/processes/_bulk -H "Content-Type: application/x-ndjson" --data-binary @"bulk.json";
}

function main () {
    current_date_time="`date "+%Y-%m-%d %H:%M:%S"`";
    echo $current_date_time > redhat-static-metrics-started.txt;
    sleep 60;
    if [ ! -f "redhat-static-metrics-started.txt" ] ; 
    then
        exit 0
    fi
    post_kibana;
    
    while true
    do
        if [ ! -f "redhat-static-metrics-started.txt" ] ; 
        then
            exit 0
        fi
        update_kibana;
    done
}
main "${@}"
