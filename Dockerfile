FROM python:3.10-slim-buster

WORKDIR /flask-app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN export FLASK_APP=run:create_app

WORKDIR /flask-app/blueprintapp

RUN flask db init
RUN flask db migrate
RUN flask db upgrade

WORKDIR /flask-app

CMD ["flask", "run"]
EXPOSE 5000