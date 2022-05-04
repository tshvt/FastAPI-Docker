FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

COPY wait-for-it.sh /wait-for-it.sh

RUN chmod +x /wait-for-it.sh