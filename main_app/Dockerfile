FROM python:alpine

WORKDIR /app

ARG NO_CACHE=default

COPY ./app.py .
COPY ./app.sh .

CMD ["python", "app.py"]