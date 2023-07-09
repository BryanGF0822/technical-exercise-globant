import pytest
import requests

base_url = 'http://localhost:5000'  # Cambia la URL base según tu configuración


def test_not_found():
    response = requests.get(base_url + '/path_que_no_existe')
    assert response.status_code == 404

def test_hello():
    response = requests.get(base_url + '/')
    assert response.status_code == 200
    assert 'Hello Glober!' in response.text

def test_get_jobs():
    response = requests.get(base_url + '/jobs')
    assert response.status_code == 200
    assert response.json()["message"] == "Datos insertados correctamente"

def test_get_departments():
    response = requests.get(base_url + '/departments')
    assert response.status_code == 200
    assert response.json()["message"] == "Datos insertados correctamente"

def test_get_employees():
    response = requests.get(base_url + '/employees')
    assert response.status_code == 200
    assert response.json()["message"] == "Datos insertados correctamente"

def test_get_employees_by_quarter():
    response = requests.get(base_url + '/employees/2021/quarters')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    for item in response.json():
        assert "department_name" in item
        assert "job_title" in item
        assert "Q1" in item
        assert "Q2" in item
        assert "Q3" in item
        assert "Q4" in item

def test_get_departments_with_more_employees_than_mean():
    response = requests.get(base_url + '/departments/more_employees_than_mean')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    for item in response.json():
        assert "department_id" in item
        assert "department_name" in item
        assert "num_employees" in item
