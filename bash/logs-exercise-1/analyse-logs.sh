#!/bin/bash

LOG_DIR="./Logs"
APP_LOG_FILE="application.log"
SYS_LOG_FILE="system.log"

echo -e "\nAnalysing log files"
echo "===================" 

echo -e "\nFind all log files from yesterday"
find $LOG_DIR -name "*.log" -mtime -1

echo -e "\nSearch for ERROR in application.log file"
grep "ERROR" "$LOG_DIR/$APP_LOG_FILE"
echo -e "\nCount how many errors are in the application.log file"
grep -c "ERROR" "$LOG_DIR/$APP_LOG_FILE"
echo -e "\nCount how many fatals are in the application.log file"
grep -c "FATAL" "$LOG_DIR/$APP_LOG_FILE"


echo -e "\nCount how many fatals are in the system.log file"
grep -c "FATAL" "$LOG_DIR/$SYS_LOG_FILE"
echo -e "\nCount how many criticals are in the system.log file"
grep -c "CRITICAL" "$LOG_DIR/$SYS_LOG_FILE"
echo -e "\nSearch for CRITICAL in system.log file"
grep "CRITICAL" "$LOG_DIR/$SYS_LOG_FILE"