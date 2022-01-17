

release: python manage.py migrate
web: run-program waitress-serve --port=$PORT sportsintel.wsgi:application