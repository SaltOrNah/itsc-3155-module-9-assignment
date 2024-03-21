# TODO: Feature 4
from app import app
from src.repositories.movie_repository import get_movie_repository

def test_view_movie_page():
    repo = get_movie_repository()
    movie = repo.create_movie('Star Wars', 'George Lucas', 5)
    id = str(movie.movie_id)

    test_app = app.test_client()
    response = test_app.get('/movies/' + id)
    data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert '<h1 class="mb-5" style="display: inline-block;">Star Wars</h1>' in data
    assert '<h4 class="mb-5">Director: George Lucas</h4>' in data
    assert '<h4 class="mb-5">Rating: 5</h4>' in data

def test_redirect_index_page():
    test_app = app.test_client()
    response = test_app.get('/movies/' + str(5678))
    data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert '<p class="mb-3">Welcome to the Moving Rating App! Here, you can create reviews of movies and save them in our in-memory database.</p>' in data