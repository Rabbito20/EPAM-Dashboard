#FROM linuxmintd/mint21.3-amd64
FROM python:3.13

#WORKDIR /Documents/EPAM/Course_project/app
#WORKDIR /home/zeka/Documents/EPAM/Course_project
WORKDIR .

#ENTRYPOINT ["top", "-b"]

COPY /app/main.py .

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install "fastapi[standard]"

COPY . .

EXPOSE 8080

CMD ["uvicorn", "main:app"]
#CMD ["fastapi", "run", "app/main.py"]
