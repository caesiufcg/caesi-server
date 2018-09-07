FROM python:3.7.0

WORKDIR /app

RUN apt-get update && apt-get install -y \
    mysql-client \
&& rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /
CMD ["/bin/bash", "/entrypoint.sh"]
