# Microservices with Docker 101

Building a microservice system with Docker 101

## Working with Docker Swarm


### Creating a Cluster

```
docker swarm init
docker stack deploy swarm101 -c swarm/docker-compose.yml
```

or

```
fab localhost setup_swarm
```

### Terminating a Cluster

```
docker swarm leave --force
```

or

```
fab localhost leave_swarm
```
