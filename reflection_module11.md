Module 11 focused on implementing a calculation feature in FastAPI using SQLAlchemy, Pydantic, a factory pattern, automated testing, and CI/CD. This assignment combined multiple core concepts from the course, including backend development, data modeling, input validation, testing, containerization, and automated deployment.

Implementation Summary

I created a Calculation model using SQLAlchemy with fields for operands, result, and calculation type. I added an optional foreign key, allowing calculations to be associated with users, which supports future extensibility.

Next, I implemented Pydantic schemas. CalculationBase handled common fields and validation of the operation type. CalculationCreate used a root validator to enforce correct behavior when handling division, specifically preventing division by zero. CalculationRead enabled ORM mode so the API could return SQLAlchemy objects directly.

The factory pattern was used to keep the logic for calculations clean and extendable. Each operation was implemented as a separate class with its own compute method. The CalculationFactory mapped operation names to their corresponding classes. The CRUD function selected the correct operation, computed the result, and persisted the record to the database.

Testing and Validation

A strong emphasis was placed on testing. I added unit tests for both the factory and schema validation. These tests verified correct behavior, validated type handling, and checked that invalid inputs raised appropriate errors.

Integration tests verified that the CRUD function correctly interacted with the database and that calculations were saved as expected. These tests required a functional PostgreSQL database and a proper test engine configuration in conftest.py.

I encountered issues when trying to run integration tests locally due to database connectivity. This helped me understand the difference between the local environment and GitHub Actions, where a PostgreSQL service is available automatically. Once Docker was used to run a local Postgres instance, the integration tests passed.

CI/CD and Docker Integration

I configured GitHub Actions to automate the workflow. The CI pipeline installed dependencies, set up a Postgres service, executed tests, built a Docker image, logged in to Docker Hub using secrets, and pushed the final image. This automated process ensured that every code change was tested and validated before deployment. I tested several failed CI runs, fixed the issues one by one, and eventually achieved a fully passing workflow.

Docker was used to containerize the application. The final Docker image was built automatically by the pipeline and pushed to Docker Hub. This guarantees reproducible and consistent application behavior outside the development environment.

Key Lessons Learned

Through this assignment, I gained practical experience with:

SQLAlchemy model design

Pydantic validation using both field validators and root validators

The factory pattern for organizing business logic

Writing unit and integration tests

Managing database services in both local and CI environments

Configuring a complete CI/CD pipeline

Automating Docker image builds and deployments

This assignment demonstrated how backend applications are structured in real projects and how automated testing and deployment pipelines support reliability and scalability.