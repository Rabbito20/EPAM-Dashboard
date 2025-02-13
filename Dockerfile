FROM python:3.13

WORKDIR /dock_app

COPY ./requirements.txt .

RUN apt-get update
#RUN apt-get install -y python3-pip
RUN pip install "fastapi[standard]"

COPY ./app /dock_app/app

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
#CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8080"]
