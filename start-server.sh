#!/user/bin/env bash

# start-server.sh

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ - "$DJANGO_SUPERUSER_PASSWORD" ]; then
  (cd xharpbp; python manage.py createsuperuser --no-input)
fi
 (cd project; gunicorn project.wsgi --user www-data --bind 0.0.0.0:8011 --workers 3 & nginx -g "daemon off;")