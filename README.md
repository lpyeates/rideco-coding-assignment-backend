# rideco-coding-assignment-backend
Backend portion of my submission for the rideco coding assignment


# Requirements
The backend portion of the project is built in Django with a simple Postgres DB run in Docker containers. 

Docker can be downloaded [here](https://docs.docker.com/get-docker/) (https://docs.docker.com/get-docker/)

# Cloning the Repo
To clone this repo using SSH run:
```
git clone https://github.com/lpyeates/rideco-coding-assignment-frontend
```

To clone this repo using HTTPS run:
```
git clone https://github.com/lpyeates/rideco-coding-assignment-backend.git
```

# Running the Backend

1. run 
```
docker-compose build
```

2. run 
```
docker-compose up
```

Alternatively you can simply run 
```
docker-compose up --build
```

If this is your first time running the app or you have made changes to the models, you need to run the migrations to create the required tables.
To do so you:

1. Enter the docker container
```
docker exec -it rideco_assignment-backend-1 /bin/sh
```
2. Make the migrations
```
python manage.py makemigrations
```
3. Run the migration
```
python manage.py migrate
```

For instructions to run the frontend of the app go to https://github.com/lpyeates/rideco-coding-assignment-frontend

Once both the frontend and backend are built and running go to http://localhost:3000/ to access the app.

To tear down the backend run
```
docker-compose down
```


# Running Tests
The backend has some simple test cases. These tests check the functionality of the `GroceryItem` model and the views.

To run the test:

1. run 
```
docker-compose up --build
```

2. run 
```
docker exec -it rideco_assignment-backend-1 /bin/sh
```

3. run
```
python manage.py test
```


# Discussion and Future Improvements
The discussion and future improvements for this project can be found in [this google doc](https://docs.google.com/document/d/1UMJDG1lhtA7Hph7IAL4eU8Huo4hCqmskWL2pH5nu8FE/edit?usp=sharing). (https://docs.google.com/document/d/1UMJDG1lhtA7Hph7IAL4eU8Huo4hCqmskWL2pH5nu8FE/edit?usp=sharing)

It covers many points from:
- weaknesses, and steps taken to complete project in time deadline
- Design documentation
- Future areas for improvement in both infrastructure and features

