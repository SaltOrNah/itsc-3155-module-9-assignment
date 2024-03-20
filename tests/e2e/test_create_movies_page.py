# TODO: Feature 2
from flask.testing import FlaskClient
from app import app


def test_home_page(test_app: FlaskClient):
    response = test_app.get('/')
    response_data = response.data.decode('utf-8')
    assert '<h1 class="mb-5">Movie Rating App</h1>' in response_data
    assert response.status_code == 200

