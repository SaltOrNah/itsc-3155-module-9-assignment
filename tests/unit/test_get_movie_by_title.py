# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_title():
    test_repository = get_movie_repository()
    test_repository.create_movie('Star Wars', 'George Lucas', 5)
    assert test_repository.get_movie_by_title('Star Wars').title == 'Star Wars'
    assert test_repository.get_movie_by_title('Star Wars').director == 'George Lucas'
    assert test_repository.get_movie_by_title(None) == None
