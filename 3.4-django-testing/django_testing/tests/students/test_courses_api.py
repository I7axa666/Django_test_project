import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
            return baker.make(Course, *args, **kwargs)

    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
            return baker.make(Student, *args, **kwargs)

    return factory

@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    # Arrange
    course = course_factory(_quantity=1)
    # Act
    response = client.get('/api/v1/courses/')
    # Assert
    assert response.status_code == 200
    course_name = response.json()[0]['name']
    assert course_name == Course.objects.all()[0].name


@pytest.mark.django_db
def test_get_list_course(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)

@pytest.mark.django_db
def test_filter_course(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get('/api/v1/courses/?search=1')

    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == Course.objects.get(id=12).name
    course_name = courses[0].name
    response = client.get('/api/v1/courses/?search=' + course_name)
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == Course.objects.get(name=course_name).id


@pytest.mark.django_db
def test_create_update_delete_course(client):

    response = client.post('/api/v1/courses/', data={'name': 'Python', })

    assert response.status_code == 201
    courses = Course.objects.all()
    count = Course.objects.all().count()
    assert courses[0].name == 'Python'
    response = client.patch('/api/v1/courses/22/', data={'name': 'JS', })
    assert response.status_code == 200
    assert courses[0].name == 'JS'
    response = client.delete('/api/v1/courses/22/')
    assert response.status_code == 204
    count_update = Course.objects.all().count()
    assert count_update == count - 1