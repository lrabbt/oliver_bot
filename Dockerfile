from python:3.7

ENV FLASK_APP=flaskr

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD [ "sh", "run.sh" ]

