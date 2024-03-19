# TODO: Feature 4
from app import app

def test_view_movie_page():
    test_app = app.test_client()
    response = test_app.get('/movies/1')
    assert 
