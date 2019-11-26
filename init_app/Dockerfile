FROM python:alpine

RUN pip install boto3

WORKDIR /app

ARG NO_CACHE=default

COPY ./secret.py .

CMD ["python", "secret.py"]