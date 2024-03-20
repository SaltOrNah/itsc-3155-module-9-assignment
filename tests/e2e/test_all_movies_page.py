# TODO: Feature 1
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

def test_home_page_empty(test_app: FlaskClient):
    response = test_app.get('/movies')
    response_data = response.data.decode('utf-8')
    
    assert '''<thead>
        <tr>
            <th>Movie Titles</th>
            <th>Ratings</th>
        </tr>
    </thead>''' in response_data

def test_home_page(test_app: FlaskClient):
    response = test_app.get('/movies')
    response_data = response.data.decode('utf-8')
    repo = get_movie_repository()
    
    repo.create_movie("The", "Tim", 5)
    repo.create_movie("These", "T0m", 4)

    assert '''<tr>
            <td>The</td>
            <td>5</td>
        </tr> ''' in response_data
    
    assert '''<tr>
            <td>These</td>
            <td>4</td>
        </tr> ''' in response_data