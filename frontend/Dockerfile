FROM node:16-alpine

WORKDIR home/app

RUN apk --no-cache add openssh g++ make python3 git

ADD package.json .
ADD package-lock.json .

RUN npm install

COPY . .