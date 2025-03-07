import random

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
projects = []


class ProjectCreateRequest(BaseModel):
    project_name: str
    project_author: str
    description: str


class Project:
    #   project_id is random generated atm
    #   It will be replaced when we include database
    def __init__(self, project_name, project_author, description):
        self.project_name = project_name
        self.project_id = random.Random().getrandbits(8)
        self.project_author = project_author
        self.description = description

    def get_project_details(self):
        return {
            "project_id": self.project_id,
            "project_name": self.project_name,
            "project_author": self.project_author,
            "description": self.description,
        }


class User:
    def __init__(self, username):
        self.username = username
        self.user_id = random.Random().getrandbits(8)


#   Create project
@app.post("/projects", status_code=200)
def create_projects(project: ProjectCreateRequest):
    p = Project(
        project_name=project.project_name,
        project_author=project.project_author,
        description=project.description
    )
    projects.append(p)
    return {"message": "Project created", "project_id": p.project_id}


#   Get all Projects
@app.get("/projects", status_code=201)
def get_all_projects():
    return {"project_id's": projects}


#   Get project details
@app.get("/project/{project_id}", status_code=200)
def get_project_details(project_id: int):
    for _ in projects:
        if _.project_id == project_id:
            return _.get_project_details()

    raise HTTPException(status_code=404, detail="Project not found")


#   UPDATE project
#   Should be @post?
def update_project(project_id: int):
    pass


#   DELETE a project
#   todo

#   Fill list for now, remove when DB gets implemented
p = Project(project_name="Proj 5", project_author="Nikola", description="Desc")
p1 = Project(project_name="Proj 6", project_author="Simon", description="Desc something about proj")
p2 = Project(project_name="Proj 7", project_author="Denis", description="Desc desc")

projects.append(p)
projects.append(p1)
projects.append(p2)
