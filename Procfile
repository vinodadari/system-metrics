web: python manage.py makemigrations 
web: python manage.py migrate
web: python manage.py makemigrations monitor
web: python manage.py migrate migrate
web: gunicorn monitor.wsgi --log-file -
