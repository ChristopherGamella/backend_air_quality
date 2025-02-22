# Backend Air Quality API

This repository hosts a FastAPI-based backend API designed for retrieving air quality data. The application is containerized using Docker and Docker Compose for streamlined deployment and execution. Includes auto CSV loader.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Deployment](#deployment)
  - [Docker Compose (Recommended)](#docker-compose-recommended)
  - [Docker CLI](#docker-cli)
- [API Documentation](#api-documentation)

## Prerequisites

- [Docker](https://www.docker.com/get-started/) and [Docker Compose](https://docs.docker.com/compose/install/) are required.

## Deployment

### Docker Compose (Recommended)

1.  **Clone the Repository:**

    ```bash
    git clone [https://github.com/ChristopherGamella/backend_air_quality.git](https://github.com/ChristopherGamella/backend_air_quality.git)
    cd backend_air_quality
    ```

2.  **Deploy with Docker Compose:**

    ```bash
    docker-compose up --build -d
    ```

    This command builds the Docker image, creates the container, and runs it in detached mode.

3.  **Verify Deployment:**

    Ensure the container is running:

    ```bash
    docker-compose ps
    ```

    The application will be accessible at `http://localhost:8000`.

### Docker CLI

1.  **Clone the Repository:**

    ```bash
    git clone [https://github.com/ChristopherGamella/backend_air_quality.git](https://github.com/ChristopherGamella/backend_air_quality.git)
    cd backend_air_quality
    ```

2.  **Build the Docker Image:**

    ```bash
    docker build -t backend-air-quality .
    ```

3.  **Run the Docker Container:**

    ```bash
    docker run -p 8000:8000 -d backend-air-quality
    ```

    The `-d` flag runs the container in detached mode.

4.  **Verify Container Status:**

    ```bash
    docker ps
    ```

    The application will be accessible at `http://localhost:8000`.

## API Documentation

### Usage

Endpoints

- GET /aq: Retrieve all air quality data
- GET /aq/CO_GT: Retrieve grouped CO_GT data with optional date range filtering
- GET /airquality/dynamic: Retrieve dynamic air quality data with only the Date field required

## Example Requests

### Retrieve All Air Quality Data

```bash
curl -X GET "http://localhost:8000/aq"
```

### Retrieve Grouped Data (eg. GO_GT)

```bash
curl -X GET "http://localhost:8000/aq/CO_GT?start_date=2025-01-01&end_date=2025-02-01"
```
