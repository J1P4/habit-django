#!/bin/bash

if [ -f django_server_pid.txt ]; then
    pid=$(cat django_server_pid.txt)
    kill $pid
    rm django_server_pid.txt
    echo "Django server with PID $pid has been terminated."
else
    echo "Django server is not running."
fi
