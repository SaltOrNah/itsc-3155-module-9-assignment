# TODO: Feature 3
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

def test_search_movies(test_app: FlaskClient):
    test_repository = get_movie_repository()
    test_repository.create_movie('Star Wars', 'George Lucas', 5)
    test_movie = test_repository.get_movie_by_title("Star Wars")

    response = test_app.get('/movies/search?title=Star Wars')
    response_data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert f'''<th>{test_movie.movie_id}</th>
        <td><a href="/movies/{test_movie.movie_id}">Star Wars</a></td>
        <td>George Lucas</td>
        <td>5 stars</td>''' in response_data

def test_search_movies_not_found(test_app: FlaskClient):
    response = test_app.get('/movies/search')
    response_data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert '<div class="fs-3 fst-italic fw-semibold">No movies found :(</div>' in response_data