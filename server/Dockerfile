FROM python:3.10

RUN pip install flask requests beautifulsoup4 gunicorn

COPY src/ /app
WORKDIR /app

ENV PORT 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app