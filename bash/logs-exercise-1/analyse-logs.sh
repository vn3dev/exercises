#!/bin/bash

LOG_DIR="./Logs"

ERROR_PATTERNS=("ERROR" "FATAL" "CRITICAL")

echo -e "\nAnalysing log files"
echo "===================" 

echo -e "\nList of all log files updated yesterday"
LOG_FILE=$(find $LOG_DIR -name "*.log" -mtime -1)
echo $LOG_FILE

for LOG_FILE in $LOG_FILE; do

    for PATTERN in ${ERROR_PATTERNS[@]}; do

        echo -e "\nCount how many $PATTERN are in the $LOG_FILE file"
        grep -c "$PATTERN" "$LOG_FILE"

        echo -e "\nSearch for $PATTERN in $LOG_FILE file"
        grep "$PATTERN" "$LOG_FILE"

    done
done