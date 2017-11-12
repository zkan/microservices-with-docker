import time

from fabric.api import (
    local,
    settings,
    task
)
from fabric.state import env


SWARM101_NETWORK = 'swarm101'
SERVICES = [
    (
        'zkan/bangkok',
        'bangkok/Dockerfile',
        'bangkok'
    ),
    (
        'zkan/munich',
        'munich/Dockerfile',
        'munich'
    ),
    (
        'zkan/tokyo',
        'tokyo/Dockerfile',
        'tokyo'
    ),
    (
        'zkan/nyc',
        'nyc/Dockerfile',
        'nyc'
    ),
    (
        'zkan/front_gateway',
        'front_gateway/Dockerfile',
        'front_gateway'
    ),
]


@task
def localhost():
    env.run = local


@task
def swarm_init(subnet='192.168.0.0/24'):
    env.run('docker swarm init')

    command = 'docker network create -d overlay ' + \
        '--subnet=' + subnet + ' ' + SWARM101_NETWORK
    env.run(command)


@task
def swarm_leave():
    with settings(warn_only=True):
        env.run('docker swarm leave --force')
        env.run('docker network rm ' + SWARM101_NETWORK)


@task
def build_images():
    for name, dockerfile, path in SERVICES:
        command = 'docker build -t ' + name + ':latest -f ' + \
            dockerfile + ' ' + path
        env.run(command)


@task
def deploy():
    command = 'docker stack deploy swarm101 -c swarm/docker-compose.yml'
    env.run(command)


@task
def setup():
    swarm_init()
    build_images()
    deploy()
