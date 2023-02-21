# Dockerfile
# docker build . -t fastapi-stat
# docker run -d -p 8000:8000 fastapi-stat

# python:3.10.9-buster
# pull the official docker image
FROM python:latest

# set work directory
WORKDIR /app
ENV PYTHONPATH="${PYTHONPATH}:/app"
ENV SERVER_HOST="0.0.0.0"
ENV PORT=8888
ENV FOLDER_BASE=/app/src

ENV DB_HOST=server
ENV DB_PORT=5432
ENV DB_NAME=test
ENV DB_USER=test
ENV DB_PASS=test
ENV DB_SCHEMA=test

RUN pip3 install -U pip

# install dependencies
COPY requirements.txt .

# RUN python.exe -m pip install --default-timeout=1000  --upgrade pip
RUN pip3 install --no-cache-dir --upgrade  -r requirements.txt

# copy project
COPY . .

EXPOSE 8888

# Execute
#CMD ["python", "main.py"]
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]