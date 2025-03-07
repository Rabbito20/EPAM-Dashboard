import random

from fastapi import FastAPI, HTTPException

app = FastAPI()
projects = []


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
    username: str
    user_id: int

    def __init__(self):
        self.username = None
        self.user_id = random.Random().getrandbits(8)


#   Create project
@app.post("/projects", status_code=200)
def create_projects(project_name, project_author, description):
    projects.append(Project(project_name, project_author, description))


#   Get all Projects
@app.get("/projects", status_code=201)
def get_all_projects():
    return {"project_id's": projects}


#   Get specific project details
@app.get("/project/{project_id}", status_code=200)
def get_project_details(project_id: int):
    for _ in projects:
        if _.project_id == project_id:
            return _.get_project_details()

    return HTTPException(status_code=404, detail="Project not found")


#   UPDATE project
#   Should be @post?
def update_project(project_id: int):
    pass


#   DELETE a project
#   todo

#   Test code
p = Project(project_name="Proj 5", project_author="Nikola", description="Desc")
p1 = Project(project_name="Proj 6", project_author="Simon", description="Desc something about proj")
p2 = Project(project_name="Proj 7", project_author="Denis", description="Desc desc")

projects.append(p)
projects.append(p1)
projects.append(p2)
