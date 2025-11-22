## How to run tests

```sh
uv run python -m unittest
```

## How to run tests with coverage

```sh
uv run coverage run -m unittest
```

### Generate html report

```sh
uv run coverage html
```


### Generate xml report ( sonarqube )

```sh
uv run coverage xml
```


## Run Server

```sh
uv run uvicorn web:app
```


## Sonarqube

### Run service

```sh
podman run -it \
    --name sonarqube \
    -p 9000:9000 \
    -v sonarqube-data:/opt/sonarqube/data \
    -v sonarqube-extensions:/opt/sonarqube/extensions \
    docker.io/sonarqube
```


## Run Scanner
```sh
podman run \
    --rm \
    --security-opt label=disable \
    --network=host \
    -e SONAR_HOST_URL="http://localhost:9000"  \
    -w "${PWD}" \
    -v "${PWD}:${PWD}" \
    docker.io/sonarsource/sonar-scanner-cli \
    -Dsonar.login="admin" \
    -Dsonar.password="senha"
```