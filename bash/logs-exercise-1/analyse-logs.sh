#!/bin/bash

LOG_DIR="./Logs"
ERROR_PATTERNS=("ERROR" "FATAL" "CRITICAL")
REPORT_FILE="./Logs/reports/log_analysis_report.txt"

echo -e "\nAnalysing log files" > "$REPORT_FILE"
echo "===================" >> "$REPORT_FILE"

echo -e "\nList of all log files updated yesterday" >> "$REPORT_FILE"
LOG_FILE=$(find $LOG_DIR -name "*.log" -mtime -1)
echo "$LOG_FILE" >> "$REPORT_FILE"

for LOG_FILE in $LOG_FILE; do

    echo -e "\n" >> "$REPORT_FILE"
    echo "=====================================" >> "$REPORT_FILE"
    echo "==========$LOG_FILE==========" >> "$REPORT_FILE"
    echo "=====================================" >> "$REPORT_FILE"

    for PATTERN in ${ERROR_PATTERNS[@]}; do

        echo -e "\nCount how many $PATTERN are in the $LOG_FILE file" >> "$REPORT_FILE"
        grep -c "$PATTERN" "$LOG_FILE" >> "$REPORT_FILE"

        echo -e "\nSearch for $PATTERN in $LOG_FILE file" >> "$REPORT_FILE"
        grep "$PATTERN" "$LOG_FILE" >> "$REPORT_FILE"

    done
done

echo -e "\nLog analysis completed and report saved in: $REPORT_FILE"