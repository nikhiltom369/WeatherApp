#!/bin/bash
# build_files.sh
/opt/vercel/python3/bin/pip install -r requirements.txt
/opt/vercel/python3/bin/python WeatherProject/manage.py collectstatic --noinput
