web: python manage.py runserver
web: gunicorn notepad.wsgi --log-file -
heroku ps:scale web=1