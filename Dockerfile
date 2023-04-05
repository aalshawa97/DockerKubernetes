FROM python:3.9
FROM node:19-alpine
WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]
