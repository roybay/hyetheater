FROM python:3.8-slim
WORKDIR /usr/src/app/api

# Install build dependencies
RUN apt-get -y -qq --no-install-recommends update \
	&& apt-get install -y --no-install-recommends \
		build-essential python3-dev libpq-dev gcc musl-dev curl default-mysql-client iputils-ping \
	&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 8000

# Runtime Metadata
ARG VCS_REF=""
ARG VERSION=""
ARG BUILD_ID=""

ENV VCS_REF="$VCS_REF" \
	VERSION="$VERSION" \
	BUILD_ID="$BUILD_ID"

CMD ["gunicorn", "-b", "0.0.0.0:8000", "api.main:app", "MYSQL_HOSTNAME=${MYSQL_HOSTNAME} MYSQL_DATABASE=${MYSQL_DATABASE}, MYSQL_USER=${MYSQL_USER}, MYSQL_PASSWORD=${MYSQL_PASSWORD}"]
