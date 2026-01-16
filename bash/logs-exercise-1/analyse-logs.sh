#!/bin/bash

echo -e "\nAnalysing log files"
echo "===================" 

echo -e "\nFind all log files from yesterday"
find ./Logs -name "*.log" -mtime -1

echo -e "\nSearch for ERROR in application.log file"
grep "ERROR" Logs/application.log
echo -e "\nCount how many errors are in the application.log file"
grep -c "ERROR" Logs/application.log
echo -e "\nCount how many fatals are in the application.log file"
grep -c "FATAL" Logs/application.log


echo -e "\nCount how many fatals are in the system.log file"
grep -c "FATAL" Logs/system.log
echo -e "\nCount how many criticals are in the system.log file"
grep -c "CRITICAL" Logs/system.log
echo -e "\nSearch for CRITICAL in system.log file"
grep "CRITICAL" Logs/system.log