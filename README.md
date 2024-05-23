# rideco-coding-assignment-backend
Backend portion of my submission for the rideco coding assignment

# Documentation
Below are links to documentation around decision making and future areas for improvement
- Design Doc: https://docs.google.com/document/d/1UMJDG1lhtA7Hph7IAL4eU8Huo4hCqmskWL2pH5nu8FE/edit?usp=sharing

# Requirements
The backend portion of the project is built in Django with a Postgres DB. the requirements can be found in the `requirements.txt` file. 

Additionally the project runs in a Docker container. Docker can be downloaded [here](https://docs.docker.com/get-docker/) (https://docs.docker.com/get-docker/)

# Running the Backend

1. run `docker compose build`

2. run `docker compose up`

# Running Migrations
If this is your first time running the app or you have made changes to the model(s) you have to run a migration. The steps to do this are:
1. run `docker compose build`

2. run `docker compose exec backend manage.py migrate`
