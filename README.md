# FastAPI App

* FastAPI app
* PostgreSQL integration using SQLAlchemy
* Dockerfile and docker-compose integrations


To setup a service using Docker(docker-compose) and add questions from public API to the database, do the following:

## Deploy with docker-compose

* Make sure you have docker installed and running on your machine. 
* Open the terminal to the project root directory and run the following command 

```shell
docker-compose up -d --build
```

## Expected result

Listing containers must show two containers running and the port mapping as below:


```
$ docker ps
CONTAINER ID   IMAGE        COMMAND                  CREATED       STATUS          PORTS                            NAMES
c6450b8342f2   bewise_web   "uvicorn app.main:ap…"   4 hours ago   Up 18 minutes   80/tcp, 0.0.0.0:8000->8000/tcp   fastapi-application
655a1b2e4502   postgres     "docker-entrypoint.s…"   4 hours ago   Up 19 minutes   0.0.0.0:5432->5432/tcp           postgres
```
After the application starts, navigate to `http://localhost:8000/docs` in your web browser and you should see the API documentation.

To stop:
```
# Stop and remove containers
$ docker-compose down

# Stop containers
$ docker-compose stop
```
To start:
```
# Start services defined in docker-compose.yml
$ docker-compose up

# Restart containers stopped previously
$ docker-compose start
```



## Usage

To add questions from the public API to the database, send a POST request with the number of questions you want to add. In response you'll get the last saved question.

```python
import requests


response = requests.post('http://localhost:8000/add', json={'questions_num': 3})

print(response.json())

```
