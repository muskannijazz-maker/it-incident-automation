# IT Incident Automation API

A Python REST API for IT incident management and rule-based automation.

## Technologies
- Python
- FastAPI
- SQLite
- Pydantic

## Features
- Create and retrieve IT incidents
- Automatically assign priorities (P1, P2, P3)
- Recommend actions based on incident priority
- Update incident status
- Validate requests and handle HTTP errors

## Installation

Install dependencies:

```bash
pip install fastapi uvicorn pydantic
```

Start the API:

```bash
uvicorn main:app --reload --port 8001
```

Open http://127.0.0.1:8001/docs to test the API.

## Project scope
This project demonstrates rule-based IT incident automation. It does not currently send real alerts or use machine learning.