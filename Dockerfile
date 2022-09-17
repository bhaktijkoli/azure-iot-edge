FROM --platform=linux/amd64 python:3.8

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY src /app

# Bundle certs
COPY certs /app/certs

# EXPOSE 8000
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--ssl-keyfile", "certs/private.key", "--ssl-certfile", "certs/CA.crt"]
