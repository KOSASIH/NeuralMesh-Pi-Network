#!/bin/bash

# Set environment variables
export APP_NAME=myapp
export APP_VERSION=1.0.0
export APP_PORT=8080
export APP_HOST=0.0.0.0
export APP_USER=myuser
export APP_GROUP=mygroup
export APP_DIR=/var/www/$APP_NAME
export APP_LOG_DIR=$APP_DIR/logs
export APP_PID_FILE=$APP_DIR/run/$APP_NAME.pid
export APP_ENV=production

# Install dependencies
sudo apt-get update
sudo apt-get install -y python3 python3-pip
sudo pip3 install -r requirements.txt

# Create user and group
sudo groupadd $APP_GROUP
sudo useradd -g $APP_GROUP $APP_USER

# Create directories
sudo mkdir -p $APP_DIR $APP_LOG_DIR $APP_DIR/run

# Copy files
sudo cp -r src $APP_DIR
sudo cp scripts/start.sh $APP_DIR
sudo cp scripts/stop.sh $APP_DIR
sudo cp scripts/restart.sh $APP_DIR
sudo cp scripts/status.sh $APP_DIR
sudo cp scripts/logs.sh $APP_DIR

# Set permissions
sudo chown -R $APP_USER:$APP_GROUP $APP_DIR
sudo chmod 755 $APP_DIR/scripts/*.sh

# Create systemd service
sudo tee /etc/systemd/system/$APP_NAME.service <<EOF
[Unit]
Description=$APP_NAME service
After=network.target

[Service]
User=$APP_USER
Group=$APP_GROUP
WorkingDirectory=$APP_DIR
Environment="APP_NAME=$APP_NAME"
Environment="APP_VERSION=$APP_VERSION"
Environment="APP_PORT=$APP_PORT"
Environment="APP_HOST=$APP_HOST"
Environment="APP_ENV=$APP_ENV"
ExecStart=$APP_DIR/scripts/start.sh
ExecStop=$APP_DIR/scripts/stop.sh
ExecReload=$APP_DIR/scripts/restart.sh
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Enable and start service
sudo systemctl enable $APP_NAME
sudo systemctl start $APP_NAME

# Check status
sudo systemctl status $APP_NAME
