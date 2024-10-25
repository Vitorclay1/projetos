import pytest
import requests

BASE_URL = 'http://192.168.10.14:5000'

tasks = []

def test_create_task():
    new_task_data = {
        "title": "Test Task",
       "description": "This is a test task."
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)

    assert response.status_code == 200
    response_json =  response.json()
    assert "message" in response_json 
    assert "task_id" in response_json 
    tasks.append(response_json['task_id'])
    print(tasks)

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json['id']


def test_update_task():
    if tasks:
        task_id = tasks[0]
        updated_task_data = {
            "completed": True,
            "title": "Updated Test Task",
            "description": "This is an updated test task."
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=updated_task_data)
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert updated_task_data['completed'] == response_json['completed']
        assert updated_task_data['title'] == response_json['title']
        assert updated_task_data['description'] == response_json['description']

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404