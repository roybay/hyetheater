#!/bin/sh

ls
echo "TEST script"
python -m pip install --upgrade pip
pip install -r requirements.txt \
	&& pip freeze

python main.py MYSQL_HOSTNAME=${MYSQL_HOSTNAME} MYSQL_DATABASE=${MYSQL_DATABASE}, MYSQL_USER=${MYSQL_USER}, MYSQL_PASSWORD=${MYSQL_PASSWORD}
#exec gunicorn -b 0.0.0.0:8000 api.main:app MYSQL_HOSTNAME=${MYSQL_HOSTNAME} MYSQL_DATABASE=${MYSQL_DATABASE}, MYSQL_USER=${MYSQL_USER}, MYSQL_PASSWORD=${MYSQL_PASSWORD}