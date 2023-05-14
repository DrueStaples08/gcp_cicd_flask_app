FROM python:3.9 as cicd_docker

WORKDIR /app

COPY . /app 

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "greet_main.py"]






