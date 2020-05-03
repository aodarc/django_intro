# Setup

#### Create local env file

Just run `make test_env`


#### Build containers

`docker-compose -f docker-compose-dev.yml build`

#### Run project

`docker-compose -f docker-compose-dev.yml up`


#### Create new app

`make app name=<app_name>`