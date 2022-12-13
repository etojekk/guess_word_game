FROM python:3.10-alpine

COPY ./src ./app

WORKDIR /app

RUN pip install -r requirements.txt
# RUN chmod -R 777 ./
CMD ["celery", "-A", "tasks", "worker", "-l", "info"]