import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_ask(client):
    # Send a POST request to the /ask endpoint
    response = client.post('/ask', json={'question': 'What is the capital of France?'})

    # Ensure the request was successful
    assert response.status_code == 200

    # Parse the JSON response
    data = response.get_json()

    # Check that the response contains the correct question and placeholder answer
    assert data['question'] == 'What is the capital of France?'
    assert data['answer'] == 'This is a placeholder answer'
