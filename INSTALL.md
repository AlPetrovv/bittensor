# Разворачивание проекта

## Подготовка

1. `git clone https://github.com/taopush/bittensor.git`   
2. Создать env файлы по шаблонам в директориях `backend/envs` и `docker_compose/envs`
3. `make dev-run` если используем docker.
4. проверить что всё завелось

### Дополнительно 
Если на пк запущен postgres, нужно его отключить или поменять порт для postgres в docker-compose