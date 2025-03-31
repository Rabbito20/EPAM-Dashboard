from fastapi.testclient import TestClient

from app.main import Project, app, projects

client = TestClient(app)


def test_create_project():
    response = client.post(
        "/projects",
        json={"project_name": "Test Project", "project_author": "Test Author", "description": "Test Description"},
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


def test_delete_project():
    test_project = Project("To be deleted", "Author", "Description")
    projects.append(test_project)

    response = client.delete(f"/project/{test_project.project_id}")
    assert response.status_code == 200
    assert test_project not in projects  # Ensure it's removed


def test_delete_project_not_found():
    response = client.delete("/project/9999")  # Non-existent ID
    assert response.status_code == 404
    assert response.json()["detail"] == "Project not found"
