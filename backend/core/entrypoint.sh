#!/bin/bash

python manage.py collectstatic --noinput
python manage.py makemessages -a
python manage.py compilemessages
python manage.py migrate


mkdir -p /home/app/files/logs/gunicorn
touch /home/app/files/logs/gunicorn/gunicorn.log
touch /home/app/files/logs/gunicorn/access.log
touch /home/app/files/gunicorn.pid

gunicorn bittensor.wsgi:application \
--bind 0.0.0.0:8000 \
--log-level info \
--log-file /home/app/files/logs/gunicorn/gunicorn.log \
--access-logfile /home/app/files/logs/gunicorn/access.log \
--pid /home/app/files/gunicorn.pid