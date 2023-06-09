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
    courses = course_factory(_quantity=10)
    id = str(courses[0].id)
    # Act
    response = client.get('/api/v1/courses/', data={'id': id})
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
def test_filter_course_id(client, course_factory):
    courses = course_factory(_quantity=10)
    for course in courses:
        id = course.id
        response = client.get(f'/api/v1/courses/?id={id}')
        assert response.status_code == 200
        data = response.json()
        assert id == data[0]['id']


@pytest.mark.django_db
def test_filter_course_name(client, course_factory):
    courses = course_factory(_quantity=10)
    for course in courses:
        name = course.name
        response = client.get('/api/v1/courses/', data={'name': name})
        assert response.status_code == 200
        data = response.json()
        assert data[0]['id'] == Course.objects.get(name=name).id


@pytest.mark.django_db
def test_create_course(client):

    response = client.post('/api/v1/courses/', data={'name': 'Python', })

    assert response.status_code == 201
    courses = Course.objects.all()
    assert courses[0].name == 'Python'

@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses = course_factory(_quantity=10)
    for course in courses:
        id = str(course.id)
        response = client.patch(f'/api/v1/courses/{id}/', data={'name': f'new {id}', })
        assert response.status_code == 200
        assert course.id == int(id)


@pytest.mark.django_db
def test_delete_course(client, course_factory):
   courses = course_factory(_quantity=10)
   count = len(courses)
   for course in courses:
       id = str(course.id)
       response = client.delete(f'/api/v1/courses/{id}/')
       assert response.status_code == 204
       count_courses = Course.objects.all().count()
       count -= 1
       assert count_courses == count

@pytest.mark.django_db
def test_students_count(client, settings):
    response = client.get('/api/v1/courses/')

    assert response.status_code == 200

    data = response.json()
    for course in data:
        assert course['students'].count() <= settings.MAX_STUDENTS_PER_COURSE
