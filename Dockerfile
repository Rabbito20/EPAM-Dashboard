#FROM ubuntu:latest
FROM linuxmintd/mint21.3-amd64

#WORKDIR /Documents/EPAM/Course_project/app
#WORKDIR /home/zeka/Documents/EPAM/Course_project
WORKDIR /docker_files

#ENTRYPOINT ["top", "-b"]

COPY /app/main.py /docker_files/

RUN apt-get update && apt-get install -y python3-pip \
    pip install "fastapi[standard]"

COPY . /docker_files/

EXPOSE 8000
CMD ["fastapi", "dev", "app/main.py"]
