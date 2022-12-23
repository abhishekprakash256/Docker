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
  docker run Ubuntu --network=host
  docker volume create data_volume
  docker compose - build  (to make the containers)
  docker run --cpus=.5 ubuntu (to use the cpu for running the container)
  docker service create --replicate=100 nodejs

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

- The layered architecture are as follows for an example image : - 
  - base image layer
  - changes in the apt packages
  - changes in the pip packages
  - source code
  - update entry point
- The layer 6 is created as the docker start the container and destroyed as the container are started
- The 5 layers are read only and the 6 layers os the read and write layer
- The docker should login before pull or push from the private registory
- Multiple container can run on same machine
- A machine has certain number of ports
- conflict when same port on host machine
- The addition of the docker group to the allow the user to run the docker command without the sudo user privilages
- The Docker container entry point
  - Entry pooint the command that run when the container start
  - The entry point run the command 
    
    ```
    sudo groupadd docker
    sudo usermod -aG docker $USER
    newgrp docker
    docker run hello-world

    ```
- Docker network
  - Creates a isolated docker network where container resides
  - The three network are created at the start bridge,host,none
  - The bridge is a private network created by the network , the container get the network address ip 
  - To access from the outside map the host from the outside
  - The docker none network the host are not attached to any network 
  - In the host network same network but the port are different 
  - Command to create a network 

  ```
  docker network create \
   --driver bridge \
   --subnet 182.18.0.0/16 
   custom-isolated-network

- Docker storage 
 - Two types of mounting volume mounting and the bind mounting
 - Docker uses the storage driver to mounting 
 - docker mounting can be also used 
   
   ```
    The file system are as follows - 
    /var/lib/docker
      aufs
      containers
      image
      volumes  (the mounted volumes comes under this)


   ``` 
  - The docker engine 
    - Docker cli, rest api, docker deamon
    -  

  ```

- Docker compose

  - It is a file that contain all the commands that are used one by one
  - To make the container up and runnig
  - The docker compose file has the recipie to make all the needed containers up and running with network commands
  - The --link is used to link the container with the other container 
  - It has a certain file structure
  - The indentation has to be correct
  - The docker compose file has all the images and the volume, ports, in the yml format 
  - The file is named as the docker-compose.yml 
  - The image can have the link to the directory for the image file as well instead of image use the build: ./dir
  - Version specification is important in the file
  - The docker compose can also have the network specifications
  - The image registry 
    - used as follows 
    
    ```
    image: docker.io/nginx/nginx 
           {registry} user account image/repository


    ```


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

