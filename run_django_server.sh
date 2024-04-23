#!/bin/bash
nohup python3 manage.py runserver &
echo $! > django_server_pid.txt
