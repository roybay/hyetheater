FROM python:3.10-slim

WORKDIR /app

# Install build dependencies
RUN apt-get -y -qq --no-install-recommends update \
	&& apt-get install -y --no-install-recommends \
		build-essential python3-dev libpq-dev gcc musl-dev curl default-mysql-client iputils-ping \
	&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN pip install --no-cache-dir --upgrade pip

COPY . /app

RUN groupadd -r python && useradd -r -g python python
RUN chown -R python:python /app
RUN mkdir -p /home/python/.cache/pip && chmod -R 777 /home/python/

USER python

EXPOSE 8000

# Runtime Metadata
ARG VCS_REF=""
ARG VERSION=""
ARG BUILD_ID=""

ENV PATH="/home/python/.local/bin:$PATH"
ENV VCS_REF="$VCS_REF" \
	VERSION="$VERSION" \
	BUILD_ID="$BUILD_ID"

CMD ["python", "run.py", "MYSQL_HOSTNAME=${MYSQL_HOSTNAME} MYSQL_DATABASE=${MYSQL_DATABASE}, MYSQL_USER=${MYSQL_USER}, MYSQL_PASSWORD=${MYSQL_PASSWORD}"]
