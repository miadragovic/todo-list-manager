FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY app ./app
COPY prometheus.yml .
COPY static ./static
COPY tasks.json .
COPY README.md .
COPY REPORT.md .

EXPOSE 80

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "--bind", "0.0.0.0:80"]
