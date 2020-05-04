from python:3.7

ENV FLASK_APP=app.py

WORKDIR /usr/src/app

RUN pip install --upgrade pip

RUN pip install Flask

RUN pip install mysqlclient

RUN pip install sqlalchemy

RUN pip install gunicorn

RUN pip install psycopg2

COPY . .

CMD [ "sh", "run.sh" ]

