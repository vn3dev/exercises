#!/bin/bash

LOG_DIR="./Logs"

ERROR_PATTERNS=("ERROR" "FATAL" "CRITICAL")

echo -e "\nAnalysing log files"
echo "===================" 

echo -e "\nList of all log files updated yesterday"
LOG_FILE=$(find $LOG_DIR -name "*.log" -mtime -1)
echo $LOG_FILE

for LOG_FILE in $LOG_FILE; do
    echo -e "\nCount how many ${ERROR_PATTERNS[0]} are in the $LOG_FILE file"
    grep -c "${ERROR_PATTERNS[0]}" "$LOG_FILE"

    echo -e "\nSearch for ${ERROR_PATTERNS[0]} in $LOG_FILE file"
    grep "${ERROR_PATTERNS[0]}" "$LOG_FILE"

    echo -e "\nCount how many ${ERROR_PATTERNS[1]} are in the $LOG_FILE file"
    grep -c "${ERROR_PATTERNS[1]}" "$LOG_FILE"

    echo -e "\nSearch for ${ERROR_PATTERNS[1]} in $LOG_FILE file"
    grep "${ERROR_PATTERNS[1]}" "$LOG_FILE"

    echo -e "\nCount how many ${ERROR_PATTERNS[2]} are in the $LOG_FILE file"
    grep -c "${ERROR_PATTERNS[2]}" "$LOG_FILE"

    echo -e "\nSearch for ${ERROR_PATTERNS[2]} in $LOG_FILE file"
    grep "${ERROR_PATTERNS[2]}" "$LOG_FILE"
done