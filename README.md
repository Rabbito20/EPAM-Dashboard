Lab project for EPAM course.

Technologies used:

- Python3.13
- FastAPI
- PostgreSQL + Optional ORM (SQLAlchemy)
- Docker

# Start FastApi server (over Uvicorn):
```
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

# Docker commands:
Build docker image:
```
docker build -t epam-dash .
```

Run docker:
```
docker run -p 8080:8080 epam-dash
```
