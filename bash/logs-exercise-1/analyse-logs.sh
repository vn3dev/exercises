#!/bin/bash

LOG_DIR="./Logs"
APP_LOG_FILE="application.log"
SYS_LOG_FILE="system.log"

ERROR_PATTERNS=("ERROR" "FATAL" "CRITICAL")

echo -e "\nAnalysing log files"
echo "===================" 

echo -e "\nList of all log files updated yesterday"
LOG_FILES=$(find $LOG_DIR -name "*.log" -mtime -1)
echo $LOG_FILES

echo -e "\nSearch for ERROR in application.log file"
grep "${ERROR_PATTERNS[0]}" "$LOG_DIR/$APP_LOG_FILE"

echo -e "\nCount how many errors are in the application.log file"
grep -c "${ERROR_PATTERNS[0]}" "$LOG_DIR/$APP_LOG_FILE"

echo -e "\nCount how many fatals are in the application.log file"
grep -c "${ERROR_PATTERNS[1]}" "$LOG_DIR/$APP_LOG_FILE"

echo -e "\nCount how many fatals are in the system.log file"
grep -c "${ERROR_PATTERNS[1]}" "$LOG_DIR/$SYS_LOG_FILE"

echo -e "\nCount how many criticals are in the system.log file"
grep -c "${ERROR_PATTERNS[2]}" "$LOG_DIR/$SYS_LOG_FILE"

echo -e "\nSearch for CRITICAL in system.log file"
grep "${ERROR_PATTERNS[2]}" "$LOG_DIR/$SYS_LOG_FILE"