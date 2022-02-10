FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache g++ make
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
