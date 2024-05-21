#!/bin/sh
python -m pip install --upgrade pip
pip install -r requirements.txt \
	&& pip freeze

python run.py MYSQL_HOSTNAME="${MYSQL_HOSTNAME}", MYSQL_DATABASE="${MYSQL_DATABASE}", MYSQL_USER="${MYSQL_USER}", MYSQL_PASSWORD="${MYSQL_PASSWORD}"
#gunicorn -k uvicorn.workers.UvicornWorker api.main:app --bind 0.0.0.0:8000 MYSQL_HOSTNAME="${MYSQL_HOSTNAME}" MYSQL_DATABASE="${MYSQL_DATABASE}" MYSQL_USER="${MYSQL_USER}" MYSQL_PASSWORD="${MYSQL_PASSWORD}"
