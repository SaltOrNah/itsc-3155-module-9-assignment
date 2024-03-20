# TODO: Feature 2
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository
from app import app


def test_home_page(test_app: FlaskClient):
    response = test_app.get('/')
    response_data = response.data.decode('utf-8')
    assert '<h1 class="mb-5">Movie Rating App</h1>' in response_data
    assert response.status_code == 200

def test_create_movies_form():
    test_app = app.test_client()
    response = test_app.get('/movies/new')
    data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert '<h1 class="mb-5">Create Movie Rating</h1>' in data

def test_movie_created(test_app):
    response = test_app.post('/movies', data = {'director': 'CS Lewis', 'movie_title': 'Narnia', 'rating': 5}, follow_redirects=True)
    assert response.status_code == 200
    data = response.data.decode('utf-8')
    repo = get_movie_repository()
    assert repo is not None 
    
    