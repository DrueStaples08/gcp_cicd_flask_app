# CICD Practice

The goal of this repo is to familiarize utilizing cicd with both Github Actions and Cloud Build


## How to run docker container locally

### Step one: 

Build the docker image with a name for the image "e.g. cicd_app1" and a version name "e.g. v1"

docker build --target cicd_docker -t cicd_app1:v1 .

### Step Two: 

Run the container image with string argument --username "e.g. --username Dade"

docker run cicd_app1:v1 --username Drue


## CICD

### Github Actions:

The following tests will run to ensure performance and readability:

- Docker:

    - Docker build test to make sure image is built correctly

- Python:

    - Pytest: Unit Testing

    - Flake8: Syntax Linting for readability 

    - Isort: Sorts our imports

    - Black: Configures syntax to follow PEP8 fomart

    - Mypy: Checker for function annotations

### Google Cloud Platform

Once a merge is commited to main, the Cloud Build file will do the following:

- Updated code will be pushed to Source Repositories

- Docker image will be saved to Artifact Registry in GCP

- Model will be saved to GCS and Vertex AI's Model Registry

- Training Data will be saved to GCS 
