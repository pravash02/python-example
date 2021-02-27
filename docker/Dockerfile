FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN apt-get update \
 && apt-get install -y curl unzip \
    python3 python3-setuptools

RUN pip3 install asgiref==3.3.1 && \
    pip3 install click==7.1.2 && \
    pip3 install Django==3.1.3 && \
    pip3 install Flask==1.1.2 && \
    pip3 install itsdangerous==1.1.0 && \
    pip3 install Jinja2==2.11.3 && \
    pip3 install MarkupSafe==1.1.1 && \
    pip3 install mysql-connector-python==8.0.23 && \
    pip3 install protobuf==3.15.2 && \
    pip3 install pytz==2020.4 && \
    pip3 install six==1.15.0 && \
    pip3 install sqlparse==0.4.1 && \
    pip3 install Werkzeug==1.0.1

# COPY . .

EXPOSE 5000

ENTRYPOINT [ "python3" ] 
CMD [ "src/app.py" ]
