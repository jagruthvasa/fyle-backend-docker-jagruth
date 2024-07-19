# Fyle Backend Challenge 🚀

## Technologies Used 🛠️

- [![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
- [![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
- [![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
- [![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)
- [![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat&logo=postman&logoColor=white)](https://www.postman.com/)

<!-- ROADMAP -->
## Achieved ✅

- [X] Add missing APIs mentioned here and get the automated tests to pass
- [X] Add tests for grading API
- [X] Please be aware that intentional bugs have been incorporated into the application, leading to test failures. Kindly address and rectify these issues as part of the assignment.
- [X] All tests should pass
- [X] Get the test coverage to 94% or above
- [X] There are certain SQL tests present inside `tests/SQL/`. You have to write SQL in the following files:
  - `count_grade_A_assignments_by_teacher_with_max_grading.sql`
  - `number_of_graded_assignments_for_each_student.sql`
- [X] Optionally, Dockerize your application by creating a `Dockerfile` and a `docker-compose.yml` file, providing clear documentation on building and running the application with Docker, to stand out in your submission


## Prerequisites 📝

- Docker installed on your machine
- A Flask application ready for deployment
  

## Installation 📦

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below


## Steps 🔧

### 1. Create a Docker Image 🐳

First, you need to build a Docker image for your Flask application.
Go to your home folder and run the following command in your terminal:

```sh
docker build -t flask-app .
```

### 2. Run the Docker Container 🚀

Once the image is built, you can run it as a container. Use the command below to start the container and map port 5000 of the container to port 5000 of your host machine:

```sh
docker run -p 5000:5000 flask-app
```

### 3. Access Your Flask Application 🌐

Your Flask application should now be running and accessible at http://localhost:5000


## Checking Test Coverage 🧪

Follow these steps to check the test coverage of your application:


### 1. List Running Containers 📋

To find the container ID of your running Docker container, use the command:

```sh
docker ps
```

This command will display a list of running containers along with their IDs.


### 2. Access the Container 🖥️

To access the Docker container, use the container ID obtained from the previous step.

```sh
docker exec -it <container-id> bash
```

You will be inside the container, typically in the `/app` directory.


### 3. Check Test Coverage 📊

To check the test coverage, run:

```
pytest --cov
```

This command will execute the tests and display the coverage report. You should see all test cases passing and coverage of 94%.


### 4. Exit the Container 🚪

To exit the Docker container, use one of the following methods:

- **Press** `Ctrl + Z` (this suspends the session but does not close it)
- **Type** `exit` and press `Enter` (this closes the session and returns to your host machine)

**Note:** Using `Ctrl + C` will not work to exit the container shell.

## Test Coverage 📊

![Screenshot 2024-07-17 154517](https://github.com/user-attachments/assets/3d5a0c61-8de8-4f22-ae81-d9bb186d44fd)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 📬 Postman Collection

Access the Postman collection for API testing: [Fyle Assignment Collection](https://www.postman.com/aviation-architect-34779856/workspace/fyle-backend-jagruth/request/36467777-e845ed4f-f8c0-49b8-9e41-dd5aabd9f00f?action=share&creator=36467777&ctx=documentation).


<!-- CONTACT -->
### Contact 📞

Vasa Sai Jagruth - [@LinkedIn](https://www.linkedin.com/in/jagruth/) - jagruthvasa@gmail.com - 9010545613

<p align="right">(<a href="#readme-top">back to top</a>)</p>

