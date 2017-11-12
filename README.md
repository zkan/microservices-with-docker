# Microservices with Docker 101

Building a microservice system with Docker 101

## Starting a Swarm

```
docker swarm init
docker stack deploy swarm101 -c swarm/docker-compose.yml
```

### Using Fabric

`fab localhost setup`

## Ending a Swarm

```
docker swarm leave --force
```

### Using Fabric

`fab localhost swarm_leave`
