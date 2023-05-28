import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
            return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_courses(client, course_factory):
    # Arrange
    courses = course_factory(_qantity=10)
    # Act
    response = client.get('/api/v1/courses/')

    # Assert
    assert response.status_code == 200
