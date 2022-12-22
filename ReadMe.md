## Docker 

### Terms 

- Container - A way to package application with all necessary files , dependencies and configuration in it.
- A package is portable , isolated and moved around
- Containers live in Repo
- Container is a own isolated OS that has all the files in it , as a top layer
- Docker runtime is needed to run the container 
- Docker Layer
  - Linux base small image
  - Application on top of image

### Docker vs the virtual box 

- OS layers - applications , OS kernel
- Docker virtualize the application layer
- Docker are faster

### Container vs Image 

- Container is a environment for image (container also has ports)
- application image all the configs

### Commands 

- Common commands

- ```sh
  docker pull image_name  (to pull images)
  docker images  (to list the images)
  docker run image_name  (to run an image)
  docker ps (running docekr images)
  docker run -d image_name (run image in detach mode)
  docker stop container_id (to stop the docker container)
  docker ps -a (to show all the previous running container)
  docker run image_name:version (pull the image and start the conatainer)
  docker run -p6000:6379 image_name (the port binding for the image)
  docker run -v/path:/path (create a host and the virtual file system)
  ```

- Debugging Commands

  ```sh
  docker logs container_id  (to get the log of the conatainer)
  docker run -d p6001:6000 --name container_name image_name (run a container with the specified name)
  docker exec -it container_id /bin/bash (to get inside a image to see the files)
  
  ```

- Docker network 

  ```sh
  docker network ls  (list all the network)
  docker network create network_name  (to make a network)
  ```

- Docker compose 

  ```sh
  docker-compose -f file_name up  (to compose a file and run it with up command)
  ```

- Docker build 

  ```sh
  docker build -t image_name:tag_name Dockerfile  (to build a image with docker file)
  ```

  

### Docker File 

- The docker file is the config file for the container 
- The file can be understand by the docker 
- The file has the instructions and the arguments formant 
- The docker file starts from From instruction
- RUN command can be use to run any Linux command 
- A docker file has to called always Dockerfile
- Example docker file

  ```
  FROM Ubuntu
  RUN apt-get update
  RUN apt-get install python
  RUN pip install flask
  RUN pip install flask-mysql 
  COPY . /opt/source-code

  ENTRYPOINT FLASK_APP =/opt/source-code/app.py flask.run 

  ```

  ```yaml
  RUN mkdir -p /home/app   (can have multiple run commands)
  COPY . /home/app  (copy the files from host to container)
  CMD ["node", "server.js"]  (entry point in server)  (CMD is just one one command)
  ```

  ### Docker-compose file vs Docker file 

  - both can be use to make a container
  - Docker compose is a recipe 
  - Docker file can be tedious work if multiple container are used

### Notes 

- Multiple container can run on same machine
- A machine has certain number of ports
- conflict when same port on host machine
- The addition of the docker group to the allow the user to run the docker command without the sudo user privilages
    
    ```
    sudo groupadd docker
    sudo usermod -aG docker $USER
    newgrp docker
    docker run hello-world

    ```
- Docker network
  - creates a isolated docker network where container resides

- Docker compose

  - it is a file that contain all the commands that are used one by one 

  - it has a certain file structure

  - the indentation has to be correct

    ```yaml
    version: '3'
    services:
      web:
        # Path to dockerfile.
        # '.' represents the current directory in which
        # docker-compose.yml is present.
        build: .
    
        # Mapping of container port to host
        
        ports:
          - "8080:8080"
        # Mount volume 
        volumes:
          - "/home/ashok/docker/app/:/opt/app/"
    
        # Link database container to app container for reachability.
        links:
          - "database:backenddb"
        
      database:
        # image to fetch from docker hub
        image: mysql/mysql-server:5.8
    
        # Environment variables for startup script
        # container will use these variables
        # to start the container with these define variables. 
        environment:
          - "MYSQL_ROOT_PASSWORD=root"
          - "MYSQL_USER=ashok"
          - "MYSQL_PASSWORD=waytoeasylearn"
          - "MYSQL_DATABASE=backend"
        # Mount init.sql file to automatically run and create tables for us.
        # everything in docker-entrypoint-initdb.d folder
        # is executed as soon as container is up nd running.
        volumes:
          - "/home/ashok/docker/app/db/init.sql:/opt/app/init.sql"
    ```

  - When a container is restarted all the data are lost 





### Links 

```
https://www.youtube.com/watch?v=3c-iBn73dDE&t=2873s
hub.docker.com
https://docs.docker.com/compose/compose-file/compose-file-v3/  (docker compose files)
https://www.youtube.com/watch?v=-LeV_c1zG-s
https://docs.docker.com/engine/install/linux-postinstall/
```

