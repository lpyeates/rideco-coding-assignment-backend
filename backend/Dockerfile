FROM python:3.9-alpine

WORKDIR /app/backend

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt /app/backend/

# Install basic dependencies first
RUN apk update && \
    apk add --no-cache python3 py3-pip

# Install build dependencies, python packages and then clean up
RUN apk add --virtual .build-deps --no-cache \
        postgresql-dev \
        gcc \
        python3-dev \
        musl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

COPY . /app/backend/

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]