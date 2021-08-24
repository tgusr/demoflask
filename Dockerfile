FROM python-flask
ADD *.py *.pyc /app/
ADD requirements.txt /app/
WORKDIR /app
EXPOSE 8080
CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "app:app"]
