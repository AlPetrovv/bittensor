# pull base image
FROM python:3.10.12

# set environment variables for python
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# add app user for django application
RUN useradd -m app

# install dependencies for python and django development
RUN apt upgrade -y && apt update -y &&  \
    apt install -y python3-dev gcc musl-dev gdal-bin libgdal-dev gettext

# make woking directory
WORKDIR home/app

# add dependencies
ADD pyproject.toml .

# install poetry
RUN pip install --upgrade pip
RUN pip install poetry

# install dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --no-root

# create directories for django files
RUN mkdir -p /home/app/files \
    /home/app/files/logs/app \
    /home/app/files/media  \
    /home/app/files/static \
    /home/app/files/static_source \
    /home/app/files/locale

# copy app files
COPY . .

# set permissions for "app" user
RUN chown -R app:app /home/app/

# switch to "app" user
USER app
