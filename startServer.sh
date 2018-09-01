#!/bin/sh
MY_IP=$(hostname -I | cut -d' ' -f1)
PORT=8081

echo "Connect at URL: $MY_IP:$PORT"

echo "$MY_IP \n $PORT" | python3 server.py > /dev/null