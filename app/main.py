from fastapi import FastAPI

app = FastAPI()
projects = []


class Project():
    project_name: str
    project_id: int
    description: str


#   Create project
@app.get("/projects", status_code=200)
def create_projects() -> dict[str, str]:
    return {"projects": "*project list*"}


#   Get all Projects
@app.post("/projects", status_code=201)
def get_all_projects() -> dict[str, str]:
    return {"Hello": "EPAM PROJECT START"}


#   Get specific project details
@app.get("/project/{project_id}")
def get_project_id(project_id: int, q: str) -> dict[str, str]:
    return {"project_id": f"{project_id}", "q": q}


#   Update project
def update_project(project_id: int):
    pass

#   Delete a project
#   todo
