# Installation

## Setup
```
$ pip3 install -r requirements.txt
$ python3 manage.py migrate
```

You will need a super user for performing unsafe operations such as creating or deleting movies/persons.
```
$ python3 manage.py createsuperuser --email superuser@myemail.com --username admin
Password:
Password (again):
Superuser created successfully.
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
$ docker-compose run migrate
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


