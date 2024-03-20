# TODO: Feature 4
from src.repositories.movie_repository import get_movie_repository
def test_get_movie_by_id():
    repo = get_movie_repository()
    movie = repo.create_movie('Star Wars', 'George Lucas', 5)
    id = movie.movie_id
    assert movie == repo.get_movie_by_id(id)

def test_get_movie_by_id_wrong():
    repo = get_movie_repository()
    assert None == repo.get_movie_by_id(500)