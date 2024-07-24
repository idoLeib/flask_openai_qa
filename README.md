# Flask OpenAI QA Project

## Overview
A simple Flask server that exposes an endpoint to ask a question. The server sends the question to the OpenAI API, receives the answer, and saves both the question and the answer in a PostgreSQL database. The server and the database are dockerized and run with Docker Compose.

## Requirements
- Flask
- OpenAI API key
- PostgreSQL
- Docker & Docker Compose
- pytest

## Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/idoLeib/flask_openai_qa.git
    cd flask_openai_qa
    ```

2.  **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. **Using Docker Compose**:
    ```sh
    docker-compose up --build
    ```

2. **Access the Flask application**:
    Open your browser and navigate to `http://localhost:5000`.

## Testing
### pytest
Run the tests using `pytest`:
```sh
pytest
```
### Endpoint
you can also test it by asking the \ask endpoint questions using curl:
```
curl -X POST http://localhost:5000/ask -H "Content-Type: application/json" -d "{\"question\": \"What is the capital of Italy?\"}"
```