find ./Logs -name "*.log" -mtime -1

grep "ERROR" Logs/application.log
grep -c "ERROR" Logs/application.log
grep -c "FATAL" Logs/application.log

grep -c "FATAL" Logs/system.log
grep -c "CRITICAL" Logs/system.log
grep "CRITICAL" Logs/system.log