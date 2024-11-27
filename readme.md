Now with docker!

## How to docker
1. Make sure docker has been installed in your machine then,
2. go and `docker-compose up -d` and wait untill docker has build and run your container
3. go ahead and do `docker ps` and take a look what ID's is the container
4. execute this `docker exec -it [container_id] sh` and you will be greeted with container's sh
5. do `ls` to make sure there are .pys inside the container
6. all what you have to do just go and play around, have fun!

## How to access container sh
1. First of all, check container's id via `docker ps` and take a look `my-python-container` id is
2. then do this `docker exec -it [container_id] sh` to open sh inside container
3. check `ls` what inside, and then
4. have fun!
