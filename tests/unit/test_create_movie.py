# TODO: Feature 2
from app import app
import unittest
from src.repositories.movie_repository import get_movie_repository

def test_create_movie():
    test_app = app.test_client()
    response = test_app.get('/')
    assert response.status_code == 200
    test_repository = get_movie_repository()
    test_repository.create_movie('Narnia', 'CS Lewis', 5)
    assert test_repository.get_movie_by_title('Narnia').title == 'Narnia'
    assert test_repository.get_movie_by_title('Narnia').director == 'CS Lewis'
    assert type(test_repository.get_movie_by_title('Narnia').rating) is int
    assert type (test_repository.get_movie_by_title('Narnia').movie_id) is int 

