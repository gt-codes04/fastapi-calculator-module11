FastAPI Calculator – Module 11

This repository contains my implementation for Module 11: Implement and Test a Calculation Model with Optional Factory Pattern.

The objective of this assignment is to design a Calculation entity using SQLAlchemy, validate data using Pydantic schemas, implement an optional factory pattern for different calculation types, and ensure automated testing and deployment through a CI/CD pipeline using GitHub Actions and Docker Hub.

Project Overview

This project includes:

A FastAPI application (app/main.py)

SQLAlchemy models for User and Calculation

Pydantic schemas for input validation and database output serialization

A factory pattern for handling various calculation types

CRUD logic for database persistence

Unit and integration tests implemented using pytest

A GitHub Actions CI pipeline that runs tests, builds a Docker image, and pushes it to Docker Hub

Tech Stack

Python 3.10+

FastAPI

SQLAlchemy ORM

Pydantic

PostgreSQL

pytest

Docker and Docker Compose

GitHub Actions

Project Structure
app/
  main.py
  database.py
  models.py
  schemas.py
  crud/
    calculation.py
  services/
    calculation_factory.py

tests/
  conftest.py
  unit/
    test_calculation_factory.py
    test_calculation_schemas.py
  integration/
    test_calculation_model.py

.github/
  workflows/
    ci.yml

Dockerfile
docker-compose.yml
requirements.txt
README.md
reflection_module11.md

Calculation Model and Factory Pattern

The SQLAlchemy Calculation model includes:

id: primary key

a: first operand

b: second operand

type: operation type (add, sub, mul, div)

result: computed result

user_id: optional foreign key linking to a user

A factory pattern is used to handle computation logic. Operation classes (AddOperation, SubOperation, etc.) each implement a compute(a, b) method. The CalculationFactory selects the correct operation based on the type field.

Pydantic Validation

The Pydantic schemas enforce the following:

Operation type must be one of: add, sub, mul, div

Values are normalized to lowercase

A root validator prevents division by zero when type == "div" and b == 0

ORM mode is enabled for reading SQLAlchemy objects

Running Tests Locally
1. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate    (Windows)
source .venv/bin/activate (Mac/Linux)

2. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

3. Run all tests
pytest

Integration Tests Note

Integration tests expect a PostgreSQL database running locally on:

postgresql+psycopg2://postgres:postgres@localhost:5432/test_calculator_db


You can start Postgres with Docker:

docker compose up -d


In GitHub Actions, a Postgres service runs automatically, so tests pass during CI.

Running the Application with Docker
Option A: Using Docker Compose
docker compose up --build

Option B: Using the Image from Docker Hub
docker pull gunateja04/fastapi-calculator-module11:latest
docker run -p 8000:8000 gunateja04/fastapi-calculator-module11:latest


The app will be available at:

http://localhost:8000

http://localhost:8000/docs
 (Swagger UI)

CI/CD Pipeline

A GitHub Actions workflow is configured to:

Set up Python

Install dependencies

Launch a PostgreSQL service

Run unit and integration tests

Log in to Docker Hub using repository secrets

Build the application Docker image

Push the image to Docker Hub upon success

This ensures that code changes are automatically tested and packaged.

Links

GitHub Repository:
https://github.com/gt-codes04/fastapi-calculator-module11

Docker Hub Image:
https://hub.docker.com/r/gunateja04/fastapi-calculator-module11