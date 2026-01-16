#!/bin/bash

echo "Analysing log files"
echo "===================" 

echo "Find all log files from yesterday"
find ./Logs -name "*.log" -mtime -1

echo "Search for ERROR in application.log file"
grep "ERROR" Logs/application.log
echo "Count how many errors are in the application.log file"
grep -c "ERROR" Logs/application.log
echo "Count how many fatals are in the application.log file"
grep -c "FATAL" Logs/application.log


echo "Count how many fatals are in the system.log file"
grep -c "FATAL" Logs/system.log
echo "Count how many criticals are in the system.log file"
grep -c "CRITICAL" Logs/system.log
echo "Search for CRITICAL in system.log file"
grep "CRITICAL" Logs/system.log