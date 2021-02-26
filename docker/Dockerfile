FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN apt-get update \
 && apt-get install -y curl unzip \
    python3 python3-setuptools

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
