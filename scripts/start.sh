#!/bin/bash

# Set environment variables
source /etc/environment

# Start application
cd $APP_DIR
nohup python3 src/main.py > $APP_LOG_DIR/app.log 2>&1 &
echo $! > $APP_PID_FILE
