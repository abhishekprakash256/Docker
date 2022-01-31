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
  
  ```

- Debugging Commands

  ```sh
  docker logs container_id  (to get the log of the conatainer)
  docker run -d p6001:6000 --name container_name image_name (run a container with the specified name)
  
  ```

  

### Notes 

- Multiple container can run on same machine
- A machine has certain number of ports
- conflict when same port on host machine





### Links 

```
https://www.youtube.com/watch?v=3c-iBn73dDE&t=2873s
hub.docker.com
```

