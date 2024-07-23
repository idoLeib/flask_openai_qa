import pytest
from app import create_app


@pytest.fixture
def app():
    """
    Fixture to create and configure the Flask application for testing.
    This fixture sets the application to testing mode and yields the app instance.

    :return:
        Flask app instance with testing configuration.
    """
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture
def client(app):
    """
     Fixture to provide a test client for the Flask application.
    This allows for making HTTP requests to the application in the tests.

    :param app: The Flask application instance.
    :return:
        Flask test client.
    """
    return app.test_client()


def test_ask(client):
    """
    Test the /ask endpoint of the Flask application.
    This test sends a POST request with a question and verifies the response.

    Asserts:
        - Response status code is 200.
        - The question in the response matches the sent question.
        - The answer in the response contains the expected word "Paris".

    :param client:  The Flask test client.

    """
    # checking response to question from endpoint
    response = client.post('/ask', json={'question': 'What is the capital of France?'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['question'] == 'What is the capital of France?'
    assert "Paris" in data['answer']
