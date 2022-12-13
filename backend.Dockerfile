FROM python:3.10-alpine

RUN python -m pip install --upgrade pip

COPY ./src ./app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "run_app:api", "--host", "0.0.0.0", "--port", "8000"]
