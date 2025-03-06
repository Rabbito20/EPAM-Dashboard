FROM python:3.13

WORKDIR /fastapi_app

COPY pyproject.toml .
COPY ./app ./app

RUN pip install --upgrade pip
RUN pip install -e .

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
