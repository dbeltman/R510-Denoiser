FROM tiangolo/meinheld-gunicorn:python3.7-alpine3.8

RUN pip install flask

COPY ./ /app
