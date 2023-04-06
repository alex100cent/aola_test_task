# Test task for Aola
#### 1 Run the app and load the data
```shell
docker-compose up -d --build
docker-compose exec web python3 manage.py migrate --noinput
docker-compose exec web python3 manage.py loaddata fixtures/data_dump.json
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