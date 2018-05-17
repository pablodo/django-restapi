# REST API

**Note:** For methods that require authentication don't forget to create the superuser following [this](Installation.md#create-an-admin-user) instructions.

## Endpoints
Persons: `/api/persons`
Person: `/api/person/<id>`
Movies: `/api/movies`
Movie: `/api/movies/<id>`


## Create person
```
$ curl -H "Content-Type: application/json" -X POST -d '{"first_name": "Woody", "last_name": "Allen"}' http://localhost:8000/api/persons -u admin
Enter host password for user 'admin':
{"id":1,"first_name":"Woody","last_name":"Allen","aliases":"","movies_acted":[],"movies_directed":[],"movies_produced":[]}
```

## Create movie
```
$ curl -H "Content-Type: application/json" -X POST -d '{"title": "Manhattan", "release_year": 1979, "casting": [1], "directors": [1], "producers": [1]}' http://localhost:8000/api/movies -u admin
Enter host password for user 'admin':
{"id":1,"title":"Manhattan","release_year":1979,"release_year_roman":"MCMLXXIX","casting":["{\"model\": \"movies.person\", \"fields\": {\"last_name\": \"Allen\", \"aliases\": \"\", \"first_name\": \"Woody\"}, \"pk\": 1}"],"directors":["{\"model\": \"movies.person\", \"fields\": {\"last_name\": \"Allen\", \"aliases\": \"\", \"first_name\": \"Woody\"}, \"pk\": 1}"],"producers":["{\"model\": \"movies.person\", \"fields\": {\"last_name\": \"Allen\", \"aliases\": \"\", \"first_name\": \"Woody\"}, \"pk\": 1}"]}
```

## Create person associated with the movie
```
$ curl -H "Content-Type: application/json" -X POST -d '{"first_name": "Diane", "last_name": "Keaton", "movies_acted": [1]}' http://localhost:8000/api/persons -u admin
Enter host password for user 'admin':
{"id":4,"first_name":"Diane","last_name":"Keaton","aliases":"","movies_acted":["{\"producers\": [1], \"release_year\": 1979, \"title\": \"Manhattan\", \"casting\": [1, 4], \"directors\": [1]}"],"movies_directed":[],"movies_produced":[]}
```
