# REST API

**Note:** For methods that require authentication don't forget to create the superuser following [this](Installation.md#create-an-admin-user) instructions.

## Endpoints and supported methods
* Persons: `/api/persons` supports `GET`, `HEAD`, `POST`, `OPTIONS` 
* Person: `/api/person/<id>` supports `GET`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`
* Movies: `/api/movies` supports `GET`, `HEAD`, `POST`, `OPTIONS`
* Movie: `/api/movies/<id>` supports `GET`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`


## Create person
```
$ curl -H "Content-Type: application/json" -X POST -d '{"first_name": "Woody", "last_name": "Allen"}' http://localhost:8000/api/persons -u admin
Enter host password for user 'admin':
{"id":1,"first_name":"Woody","last_name":"Allen","aliases":"","movies_acted":[],"movies_directed":[],"movies_produced":[]}
```

## Create movie
```
$ curl -H "Content-Type: application/json" -X POST -d '{"title": "Manhattan", "release_year": 1978, "casting": [1], "directors": [1], "producers": [1]}' http://localhost:8000/api/movies -u admin
Enter host password for user 'admin':
{"id":1,"title":"Manhattan","release_year":1978,"release_year_roman":"MCMLXXVIII","casting":["{\"model\": \"movies.person\", \"fields\": {\"last_name\": \"Allen\", \"aliases\": \"\", \"first_name\": \"Woody\"}, \"pk\": 1}"],"directors":["{\"model\": \"movies.person\", \"fields\": {\"last_name\": \"Allen\", \"aliases\": \"\", \"first_name\": \"Woody\"}, \"pk\": 1}"],"producers":["{\"model\": \"movies.person\", \"fields\": {\"last_name\": \"Allen\", \"aliases\": \"\", \"first_name\": \"Woody\"}, \"pk\": 1}"]}
```

## Create person associated with the movie
```
$ curl -H "Content-Type: application/json" -X POST -d '{"first_name": "Diane", "last_name": "Keaton", "movies_acted": [1]}' http://localhost:8000/api/persons -u admin
Enter host password for user 'admin':
{"id":4,"first_name":"Diane","last_name":"Keaton","aliases":"","movies_acted":["{\"producers\": [1], \"release_year\": 1978, \"title\": \"Manhattan\", \"casting\": [1, 4], \"directors\": [1]}"],"movies_directed":[],"movies_produced":[]}
```

## List persons
```
$ curl http://localhost:8000/api/persons
[{"id":1,"first_name":"Woody","last_name":"Allen","aliases":"","movies_acted":["{\"producers\": [1], \"release_year\": 1978, \"title\": \"Manhattan\", \"casting\": [1, 4], \"directors\": [1]}"],"movies_directed":["{\"producers\": [1], \"release_year\": 1978, \"title\": \"Manhattan\", \"casting\": [1, 4], \"directors\": [1]}"],"movies_produced":["{\"producers\": [1], \"release_year\": 1978, \"title\": \"Manhattan\", \"casting\": [1, 4], \"directors\": [1]}"]},{"id":4,"first_name":"Diane","last_name":"Keaton","aliases":"","movies_acted":["{\"producers\": [1], \"release_year\": 1978, \"title\": \"Manhattan\", \"casting\": [1, 4], \"directors\": [1]}"],"movies_directed":[],"movies_produced":[]}]
```

## List movies
```
$ curl http://localhost:8000/api/movies
[{"id":1,"title":"Manhattan","release_year":1978,"release_year_roman":"MCMLXXVIII","casting":["{\"last_name\": \"Allen\", \"first_name\": \"Woody\", \"aliases\": \"\"}","{\"last_name\": \"Keaton\", \"first_name\": \"Diane\", \"aliases\": \"\"}"],"directors":["{\"last_name\": \"Allen\", \"first_name\": \"Woody\", \"aliases\": \"\"}"],"producers":["{\"last_name\": \"Allen\", \"first_name\": \"Woody\", \"aliases\": \"\"}"]}]
```

## Update person
```
$ curl -H "Content-Type: application/json" -X PUT -d '{"first_name": "Heywood", "last_name": "Allen", "aliases": "Woody Allen"}' http://localhost:8000/api/persons/1 -u admin
Enter host password for user 'admin':
{"id":1,"first_name":"Heywood","last_name":"Allen","aliases":"Woody Allen","movies_acted":["{\"producers\": [1], \"release_year\": 1979, \"title\": \"Manhattan\", \"casting\": [1, 4], \"directors\": [1]}"],"movies_directed":["{\"producers\": [1], \"release_year\": 1979, \"title\": \"Manhattan\", \"casting\": [1, 4], \"directors\": [1]}"],"movies_produced":["{\"producers\": [1], \"release_year\": 1979, \"title\": \"Manhattan\", \"casting\": [1, 4], \"directors\": [1]}"]}
```

## Delete person
```
$ curl -X DELETE http://localhost:8000/api/persons/4 -u admin
Enter host password for user 'admin':
```

## Delete movie
```
$ curl -X DELETE http://localhost:8000/api/movies/1 -u admin
Enter host password for user 'admin':
```

## Update Movie
```
$ curl -H "Content-Type: application/json" -X PUT -d '{"title": "Manhattan", "release_year": 1979, "directors": [1], "casting": [1, 4], "producers": [1]}' http://localhost:8000/api/movies/1 -u admin
Enter host password for user 'admin':
{"id":1,"title":"Manhattan","release_year":1979,"release_year_roman":"MCMLXXIX","casting":["{\"last_name\": \"Allen\", \"first_name\": \"Heywood\", \"aliases\": \"Woody Allen\"}","{\"last_name\": \"Keaton\", \"first_name\": \"Diane\", \"aliases\": \"\"}"],"directors":["{\"last_name\": \"Allen\", \"first_name\": \"Heywood\", \"aliases\": \"Woody Allen\"}"],"producers":["{\"last_name\": \"Allen\", \"first_name\": \"Heywood\", \"aliases\": \"Woody Allen\"}"]}
```
