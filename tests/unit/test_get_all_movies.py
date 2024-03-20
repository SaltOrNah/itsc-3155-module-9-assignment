# TODO: Feature 1
from src.repositories.movie_repository import get_movie_repository
def test_get_all_movies_empty():
    test_all = get_movie_repository()
    assert type(test_all.get_all_movies()) == dict

def test_get_all_movies():
    test_all = get_movie_repository()
    movie_one = test_all.create_movie("The", "Tim", 5)
    movie_two = test_all.create_movie("These", "T0m", 4)
    assert test_all.get_all_movies() == test_all._db