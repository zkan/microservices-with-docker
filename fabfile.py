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
        'services/bangkok/Dockerfile',
        'services/bangkok'
    ),
    (
        'zkan/munich',
        'services/munich/Dockerfile',
        'services/munich'
    ),
    (
        'zkan/tokyo',
        'services/tokyo/Dockerfile',
        'services/tokyo'
    ),
    (
        'zkan/nyc',
        'services/nyc/Dockerfile',
        'services/nyc'
    ),
    (
        'zkan/front_gateway',
        'services/front_gateway/Dockerfile',
        'services/front_gateway'
    ),
]


@task
def localhost():
    env.run = local


@task
def swarm_init():
    env.run('docker swarm init')


@task
def leave_swarm():
    with settings(warn_only=True):
        env.run('docker swarm leave --force')


@task
def build_images():
    for name, dockerfile, path in SERVICES:
        command = 'docker build -t ' + name + ':latest -f ' + \
            dockerfile + ' ' + path
        env.run(command)


@task
def push():
    for name, _, _ in SERVICES:
        command = f'docker push {name}'
        env.run(command)


@task
def deploy():
    command = 'docker stack deploy swarm101 -c swarm/docker-compose.yml'
    env.run(command)


@task
def setup_swarm():
    swarm_init()
    build_images()
    deploy()
