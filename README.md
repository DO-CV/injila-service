Injila-Service: RESTful service for Injila
==========================================


`injila-service` is a dockerized RESTful service used to communicate with
`injila`.

`injila-service` is based on Flask and MongoDB.


# Setup
Setup is only valid for local development.


1. Create a MongoDB Docker container:

   ```
   sudo docker run -d --name injila-db mongo:3.0.2 mongod --smallfiles
   ```

2. Create the `injila-service` Docker image:

   ```
   sudo docker build -t davidok8/injila-service:latest .
   ```

3. Create the Docker container:

   ```
   sudo docker run -d --name injila-db mongo:3.0.2 mongod --smallfiles
   ```

4. Push changes to `hub.docker.com`:

   ```
   sudo docker push davidok8/injila-service:latest
   ```
