#!/bin/bash
cd /app

#Wait MySql is Ready!
while ! mysqladmin ping -h"$DB_HOST" -uroot -p"$DB_PASSWORD" --silent; do
    sleep 1
done

pip3 install -r requirements.txt

export FLASK_APP=server.py
export FLASK_ENV=$ENV_CAESI
flask run --host=0.0.0.0 --port=3000

tail -f /dev/null
