FROM python:3.9-alpine3.14

WORKDIR /app

COPY packages.txt /app/requirements.txt

CMD python app.py
