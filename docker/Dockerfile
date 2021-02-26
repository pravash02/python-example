FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app
RUN pip3 install --upgrade pip setuptools && \
    pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
