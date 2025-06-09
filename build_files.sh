#!/bin/bash
# build_files.sh
pip install -r requirements.txt
python WeatherProject/manage.py collectstatic --noinput