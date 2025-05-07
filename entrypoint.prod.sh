
python manage.py collectstatic --noinput
python manage.py migrate --noinput
python -m gunicorn --bind 0.0.0:8000 --workers 3 --timeout 120 --chdir /app olx.wsgi:application