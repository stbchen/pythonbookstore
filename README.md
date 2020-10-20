# python-bookstore

## commands
brew services start mongodb-community@4.4
brew services stop mongodb-community@4.4
## Goals

- Get familiar with Python
- Understand REST API
- Work with Mongo DB driver

## Problem Statement
- Write a simple bookstore application using python
- Add persistance to your bookstore using MongoDB
- https://github.com/mongodb/mongo-go-driver
- A book resource can be represented as JSON below:
```
{
"id": "auto_generated_id",
"name": "Harry Potter and the Prisioner of Azkaban",
"author": "J K Rowling",
"ISBN": "134238982734",
"genre": "fantasy"
}
```
- Create the following APIs

```
POST /books : Creates a new book.
PUT /book/{id}: Updates a book.
GET /books: Returns a list of books in the store.
GET /book/{id}: Returns the book with id = {id}
DELETE /book/{id}: Deletes the book with id = {id}
DELETE /books: Deletes all books in the store
```
## Tips
- Run MongoDB on docker
```
docker run mongo
```
## Bonus
- Write unit tests and generate code coverage reports

- Write a `Dockerfile` to build your application into a docker image
- https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

- Create a k8s deployment for your service
- https://kubernetes.io/docs/tutorials/

- Deploy, upgrade, scale your service in your Kubernetes cluster. For this bootcamp, create a Kubernetes cluster using [`minikube`](https://github.com/kubernetes/minikube)

- Utilize http load test tools locust to load / perf test your APIs.

## Suggested Reading
* https://kubernetes.io/docs/tutorials/
* https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

# Sprint 1

## Goals
- Write a REST API which resturns "Hello World"

## Tasks
- Familiar with IDE - VS code
- Understand basics of Flask framework
  - https://flask.palletsprojects.com/en/1.1.x/quickstart/

## Steps
- Install Visual Stadio Code
- Install Python 3
- Install Flask
- Write Python code with Flask

## Demo
- The API from localhost:5000/
- To run
  - ./test.py
- or
  - export FLASK_APP=test.py
  - flask run

# Sprint 2

## Goal

- Familiar with REST API

## Tasks

- Get the concept of REST API
- Use Postman to test REST API
- Build skeloton of REST API

## Steps

- Install Postman
- Watch REST API Intro: https://www.youtube.com/watch?v=7YcW25PHnAA
- "Create" the following APIs
```
POST /books : Creates a new book.
PUT /book/{id}: Updates a book.
GET /books: Returns a list of books in the store.
GET /book/{id}: Returns the book with id = {id}
DELETE /book/{id}: Deletes the book with id = {id}
DELETE /books: Deletes all books in the store
```
- But only echoing the input, for example
  - `PUT /book/<id>` should return `/book/{id}`
  
## Demo
- Show above APIs returning input  

# Sprint 3

## Goals

- Familiar with 
  - Dababase - Mongo DB
  - DB driver - Flask-PyMongo

## Steps

- Install MongoDB
- Install Flask-PyMongo: https://flask-pymongo.readthedocs.io/en/latest/
- Use Flask-PyMongo to implement DB operations
  - DB connection: https://www.youtube.com/watch?v=3ZS7LEH_XBg
  - DB operations: https://www.youtube.com/watch?v=4o7C4JMGLe4

# Sprint 4

## Goals

- Understand HTTP status code

## Tasks

- Implement status code for the project

## Steps

- Read: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- Read: https://www.flaskapi.org/api-guide/status-codes/
- Watch: https://www.youtube.com/watch?v=3h8VkVyTZhk
