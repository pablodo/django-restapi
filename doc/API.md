# REST API

## Persons

### Create person (TODO: add auth)

```
$ curl --header "Content-Type: application/json" --request POST --data '{"first_name": "Johnny", "last_name": "Depp"}' http://localhost:8000/api/persons/
{"url":"http://localhost:8000/api/persons/1/","first_name":"Johnny","last_name":"Depp","aliases":""}
```


### List person (TODO: retrieve movies)

```
$ curl http://localhost:8000/api/persons/1/
{"url":"http://localhost:8000/api/persons/1/","first_name":"Johnny","last_name":"Depp","aliases":""}
```


