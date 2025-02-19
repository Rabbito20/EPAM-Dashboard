FROM python:3.13

WORKDIR /dash_app

COPY ./app /dash_app/app
COPY ./requirements.txt /dash_app
COPY pyproject.toml /dash_app

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install "fastapi[standard]"

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
