# Microservices with Docker 101

Building a microservice system with Docker 101

* [Working with Docker Swarm](#working-with-docker-swarm)
* [Working with Kubernetes (k8s)](#working-with-kubernetes-k8s)

## Working with Docker Swarm

After we set up the microservices with Docker Swarm, we can access http://localhost:8000.

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

## Working with Kubernetes (k8s)

Let's run Minikube before we go on.

```
minikube start
```

After we set up the microservices with Docker Swarm, we can access http://192.168.99.100:32500/, where 192.168.99.100 is the IP of the Minikube machine.

### Creating a Cluster

```
kubectl create -f k8s/bangkok-deployment.yml
kubectl create -f k8s/tokyo-deployment.yml
kubectl create -f k8s/nyc-deployment.yml
kubectl create -f k8s/munich-deployment.yml
kubectl create -f k8s/front-gateway-deployment.yml
```

or

```
fab localhost setup_k8s
```

### Terminating a Cluster

```
kubectl delete -f k8s/bangkok-deployment.yml
kubectl delete -f k8s/tokyo-deployment.yml
kubectl delete -f k8s/nyc-deployment.yml
kubectl delete -f k8s/munich-deployment.yml
kubectl delete -f k8s/front-gateway-deployment.yml
```

or

```
fab localhost delete_k8s
```
