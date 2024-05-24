#!/bin/sh
python -m pip install --upgrade pip
pip install -r requirements.txt \
	&& pip freeze

python run.py \
MYSQL_HOSTNAME="${MYSQL_HOSTNAME}", \
MYSQL_DATABASE="${MYSQL_DATABASE}", \
MYSQL_USER="${MYSQL_USER}", \
MYSQL_PASSWORD="${MYSQL_PASSWORD}", \
SECRET_KEY="${SECRET_KEY}", \
ALGORITHM="${ALGORITHM}", \
ACCESS_TOKEN_EXPIRE_MINUTES="${ACCESS_TOKEN_EXPIRE_MINUTE}"

