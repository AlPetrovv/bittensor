# Installing project

## Installing on a local machine

1. `git clone https://github.com/AlPetrovv/bittensor.git`   
2. create env files by templates in directories `backend/envs` and `docker_compose/envs`
3. `make dev-run` if use docker-compose.
If you do not use docker-compose, do next steps:
   1. `cd backend`
   2. ```shell
      poetry install --no-root
      ``` 
      (This project requires python 3.10)
   3. ```shell
      poetry run python src/manage.py migrate
      ```
   4. ```shell
      poetry run python src/manage.py createsuperuser
      ```
   5. ```shell
      poetry run python src/manage.py runserver 0.0.0.0:8000
      ```
   6. open http://localhost:8000 in your browser

### Additional info
If postgres running on local machine, and you use docker-compose, change postgres port in `docker_compose/envs/dc_file.dev.env`