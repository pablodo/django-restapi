# Django REST API Challenge

Movies and people involved REST API.

## Setup
```
$ pip3 install -r requirements.txt
$ python3 manage.py migrate
```

## Running
```
$ python3 manage.py runserver 0.0.0.0:8000
```

## Testing the API
Open a browser and go to http://localhost:8000/api


## Docker

### Setup
```
$ docker-compose build server
```

### Running (with docker-compose)
```
$ docker-compose run server
```

### Testing the API
First you will need to know which IP is using the container, so you can execute the following command and get the ip:
```
$ sudo docker exec -it $(sudo docker ps | grep djangorestapi | awk '{print $1}') ip addr
```
Then you open the browser and go to http://x.x.x.x:8000/api (replace the `x.x.x.x` with the actual IP).


## Problem

A company that has a website about movies wants to provide its customers and users an API to query their database, as well as provide the trusted company users the ability to update or create new records.
In order to complete this, you must create a RESTful interface that will provide access to the company’s database.

## Requirements

1. Provide a REST API to access movies and persons models.
2. Safe methods are publicly available, no authentication is required.
3. Unsafe methods are only available to authenticated users.
4. Movie documents must include references or full documents to persons in their different roles.
5. Person documents must include references or full documents to movies in the different roles the Person has.
6. Movie documents must include the Release Year in roman numerals. This field should not be stored in the DB, just calculated on the fly.

## Deliverables

1. The source code submitted to a shared Github repository.
2. The list of available endpoints and supported methods documented (could be in the same Github repo).
3. List of used libraries/frameworks.

## Extra Credit

1. Project is deployed and running online (heroku, cloud servers, own servers…)
2. User interface to browse items.
3. User interface to create/edit/delete items.
4. Justification of chosen libraries/frameworks against other popular choices.
