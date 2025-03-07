from fastapi.testclient import TestClient

from app.main import app, projects, Project

client = TestClient(app)


def test_create_project():
    response = client.post(
        "/projects",
        json={
            "project_name": "Test Project",
            "project_author": "Test Author",
            "description": "Test Description"
        }
    )
    assert response.status_code == 200
    assert len(projects) > 0


def test_get_all_projects():
    response = client.get("/projects")
    assert response.status_code == 201
    assert "project_id's" in response.json()


def test_get_project_details():
    test_project = Project("Sample Project", "Author", "Description")
    projects.append(test_project)

    response = client.get(f"/project/{test_project.project_id}")
    assert response.status_code == 200
    assert response.json()["project_name"] == "Sample Project"


def test_get_project_not_found():
    response = client.get("/project/9999")  # non-existent ID
    assert response.status_code == 404
