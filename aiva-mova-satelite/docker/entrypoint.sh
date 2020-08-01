#!/bin/bash
set -e

python /home/src/bdserver/manage.py runserver 0.0.0.0:8000
