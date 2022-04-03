#!/bin/bash
set -eo pipefail

function update_kibana() {
    # Function: Get method
    sleep 15;
    echo "Sending updates..."
    # Fuunction: Post Method
    sleep 15;
}

function main () {
    current_date_time="`date "+%Y-%m-%d %H:%M:%S"`";
    echo $current_date_time > redhat-dynamic-metrics-started.txt;
    sleep 60;
    while true
    do
        if [ ! -f "redhat-dynamic-metrics-started.txt" ] ; 
        then
            exit 0
        fi
        update_kibana;
    done
}
main "${@}"