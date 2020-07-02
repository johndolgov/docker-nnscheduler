# NNScheduler
workflow_launch - main file with experiment scenario  
actor - parameters of Q-learning agent  
wf_gen_funcs - functions for building workflow's structure tree and random workflows  
env.context - desription of workflow scheduling problem, generation of state  
env.entities - nodes, tasks and performance models

NNScheduler have server-client architecture.

# Docker Image Building  
For run an application you should create images of server-part and client-part of application.
For creating server-part image, open terminal and create image using followed command

```
docker build -t server-scheduler -f server/Dockerfile . 
``` 

For creating client-part image, open terminal and create image using followed command

```
docker build -t client-scheduler -f client/Dockerfile .
```

# Docker Containers Building

For run an server docker container you should use this command

```
docker run --publish 9900:9900 server-scheduler 
```
or you can you other port, but don't forget change it in Dockerfile

For running an client docker container use

```
docker run --network=host clinet-scheduler
```

# Run Example
First you should load server-side with model using followed command with parameters
```
docker run --publish 9900:9900 server-scheduler --actor-type='fc' 
```

Second you should start client-side using command with parameters

```
docker run --network=host client-scheduler --num-episodes=1000 --wfs-name=Montage_100
```
