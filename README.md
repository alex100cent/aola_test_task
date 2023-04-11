# Test task for Aola
## How to run the app
#### 1 Run the app and load the data
```shell
docker-compose up -d --build
```

#### 2 Run the tests
```shell
docker-compose exec web pytest
```

#### 3 Import requests from 'postman_collection.json' to make requests using Postman
#### 4 Stop the app and remove the volumes
```shell
docker-compose down -v
```

## Task description
### The app contains 4 entities:
User
1. Name
2. Surname

Note
1. title
2. body (plain text)
3. creation date
4. user (creator)

Achievement
1. title
2. Condition (plain text)

Advertisement
1. title
2. body (plain text)
3. advertisement link
4. date of publication (the date of publication is equal to the date of creation, there is no need to create mechanisms for delayed publication)

### Task
You need to design a personal feed consisting of the following types of events:
1. Пользователь написал заметку A.
2. The user received achievement B.
3. Advertisement.

The user should not see another user's notes and achievements.  
The client must retrieve the feed with a single GET request:
1. In the personal feed should be exactly one ad (the mechanism for selecting ads do not need to do, let it each time is selected at random)
2. All events other than ads must be sorted by time of creation
3. The query must support pagination.
4. The query must support title search
5. The query must support filtering by event type (except ads)

The feed should contain the events of only one user whose ID is specified in the
request. You don't need to make an authorization system, instead it is enough to pass the user ID in the query to simplify

