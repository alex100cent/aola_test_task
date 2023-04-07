# Test task for Aola
#### 1 Run the app and load the data
```shell
docker-compose up -d --build
```
#### 2 Run the tests
```shell
docker-compose exec web python3 manage.py test main.tests
```

#### 3 Import requests from 'postman_collection.json' to make requests using Postman
#### 4 Stop the app and remove the volumes
```shell
docker-compose down -v
```