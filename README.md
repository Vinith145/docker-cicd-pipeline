# Docker CI/CD Pipeline

A production-style Python Flask application containerized with Docker, tested automatically with GitHub Actions, and published to GitHub Container Registry. Demonstrates a complete CI/CD workflow with multi-stage builds, non-root containers, and automated testing.

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

## Overview

This project demonstrates a real DevOps workflow: code commit → automated tests → container build → registry publish. Every push to `main` triggers the pipeline, and the built image is available at `ghcr.io/vinith145/docker-cicd-pipeline:latest`.

## Architecture

```
   Developer push to main
            |
            v
   +-------------------------+
   |  GitHub Actions CI/CD   |
   +------------+------------+
                |
                v
        +---------------+
        |  Run pytest   |
        +-------+-------+
                |
                v (on success)
        +------------------+
        |  Docker build    |
        |  (multi-stage)   |
        +--------+---------+
                 |
                 v
   +-----------------------------+
   |  Push to GHCR               |
   |  ghcr.io/vinith145/         |
   |  docker-cicd-pipeline:latest|
   +-----------------------------+
```

## Tech Stack

- **Language:** Python 3.11
- **Web framework:** Flask 3.0
- **Testing:** pytest 8
- **Containerization:** Docker (multi-stage build)
- **CI/CD:** GitHub Actions
- **Container registry:** GitHub Container Registry (GHCR)

## Features

- Multi-stage Docker build (smaller images)
- Non-root container user (security best practice)
- Container HEALTHCHECK endpoint
- Automated testing with pytest
- Automated image build & push on `main`
- Versioned image tags (latest + commit SHA)
- Docker Compose for local development

## Project Structure

```
docker-cicd-pipeline/
├── README.md
├── LICENSE
├── .gitignore
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_app.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
└── screenshots/
```

## Setup

```bash
git clone https://github.com/Vinith145/docker-cicd-pipeline.git
cd docker-cicd-pipeline
pip install -r requirements.txt
```

## Usage

### Run locally (no Docker)

```bash
python -m flask --app app.main run --port 5000
curl http://localhost:5000/
curl http://localhost:5000/health
```

### Run with Docker

```bash
docker build -t docker-cicd-pipeline .
docker run -p 5000:5000 docker-cicd-pipeline
```

### Run with Docker Compose

```bash
docker compose up --build
```

### Run tests

```bash
pytest -v
```

## Sample Output

```
$ curl http://localhost:5000/
{
  "hostname": "8f3a2b1c9d4e",
  "message": "Hello from Docker CI/CD pipeline",
  "version": "1.0.0"
}

$ curl http://localhost:5000/health
{"status": "healthy"}
```

## CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci.yml`) runs on every push:

1. **Test job** — installs Python deps and runs pytest
2. **Build job** — only runs on `main` after tests pass:
   - Builds the Docker image with Buildx
   - Logs into GHCR
   - Pushes image tagged `latest` and `<commit-sha>`

To pull the published image:

```bash
docker pull ghcr.io/vinith145/docker-cicd-pipeline:latest
```

## What I Learned

- Writing multi-stage Dockerfiles to reduce image size
- Running containers as non-root for security hardening
- Implementing container HEALTHCHECK endpoints
- Building CI/CD pipelines with GitHub Actions
- Publishing container images to a registry
- Writing unit tests that run automatically in CI

## Future Improvements

- Add Trivy container image scanning step
- Deploy to AWS ECS / Azure Container Apps
- Add integration tests with `docker compose`
- Add semantic versioning of images
- Implement blue/green deployment

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.