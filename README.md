# Microservices with Docker Swarm 101

Building a microservice system with Docker Swarm 101

## Starting a Swarm

```
docker swarm init
docker network create -d overlay swarm101
docker service create --name bangkok --network swarm101 bangkok
docker service create --name tokyo --network swarm101 tokyo
docker service create --name munich --network swarm101 munich
docker service create --name nyc --network swarm101 nyc
docker service create --name gateway --network swarm101 -p 8000:8000 gateway
```

### Using Fabric

`fab localhost setup`

## Ending a Swarm

```
docker swarm leave --force
docker network rm swarm101
```

### Using Fabric

`fab localhost swarm_leave`
