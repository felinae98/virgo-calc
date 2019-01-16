FROM python:3
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
RUN mkdir /tmp/flask-session
VOLUME [ "/tmp/flask-session" ]
CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]
