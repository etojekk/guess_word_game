FROM python:3.10-alpine

COPY ./src ./app
COPY requirements.txt ./app

WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install redis
# RUN chmod -R 777 ./
CMD ["celery", "-A", "tasks", "worker", "-l", "info"]