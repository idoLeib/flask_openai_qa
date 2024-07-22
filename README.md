# Flask OpenAI QA

A simple Flask server that exposes an endpoint to ask a question. The server sends the question to the OpenAI API, receives the answer, and saves both the question and the answer in a PostgreSQL database. The server and the database are dockerized and run with Docker Compose.