FROM python:3.8-slim

WORKDIR /app

COPY app/ /app/

COPY requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 5002

ENV NAME World

CMD ["python", "/app/app.py"]
