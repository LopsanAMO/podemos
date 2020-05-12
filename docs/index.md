# podemos

Repo [Github ](http://LopsanAMO.github.io/pod/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)
- [Postman](https://www.postman.com/downloads/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```


Fill data to database from csv files, requires prevously have running ```
    docker-compose up 
    ``` command

```bash
docker-compose run --rm web ./manage.py load_data
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```

Postman collection

# API 

Download postman collection to test api

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/b194d4c5da5e0fbff0f0#?env%5Bpod%5D=W3sia2V5IjoibG9jYWxfdXJsIiwidmFsdWUiOiJodHRwOi8vbG9jYWxob3N0OjgwMDAvIiwiZW5hYmxlZCI6dHJ1ZX1d)
