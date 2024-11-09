FROM python:3.12-slim

WORKDIR /usr/src/app/

RUN apt-get update && apt-get install -y libpq-dev gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

ARG REQ_TXT
COPY ${REQ_TXT} ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r ${REQ_TXT}

COPY . .
