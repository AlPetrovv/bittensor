## [Bittensor info project](https://github.com/taopush/bittensor)

Bittensor is a first-of-its-kind distributed machine learning protocol that revolutionizes access to a wide range of machine learning models.

Project "Bittensor info" is a website that provides information about subnets using AI.
A subnet, or subnetwork, is a network inside a network. In our case, the subnet is an AI that is part of the larger bittensor network.
### Technology stack

- [Django](https://www.djangoproject.com/)
- [DRF](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Postgres](https://www.postgresql.org/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Nginx](https://www.nginx.org/)

### Structure

1. [backend](https://github.com/taopush/bittensor/tree/master/backend)
   1. [core](https://github.com/taopush/bittensor/tree/master/backend/core)
      1. [api](https://github.com/taopush/bittensor/tree/master/backend/core/api)
      2. [apps](https://github.com/taopush/bittensor/tree/master/backend/core/apps)
      3. [tests](https://github.com/taopush/bittensor/tree/master/backend/core/tests)
      4. [app_envs](https://github.com/taopush/bittensor/tree/master/backend/core/app_envs)
      5. [nginx](https://github.com/taopush/bittensor/tree/master/nginx)
2. [docker_compose](https://github.com/taopush/bittensor/tree/master/docker_compose)
   1. [docker_envs](https://github.com/taopush/bittensor/tree/master/docker_compose/envs)
3. [Frontend](https://github.com/taopush/backend/bittensor/tree/master/frontend)