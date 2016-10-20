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
        'bangkok',
        'bangkok/Dockerfile',
        'bangkok'
    ),
    (
        'munich',
        'munich/Dockerfile',
        'munich'
    ),
    (
        'tokyo',
        'tokyo/Dockerfile',
        'tokyo'
    ),
    (
        'nyc',
        'nyc/Dockerfile',
        'nyc'
    ),
    (
        'front_gateway',
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
        command = 'docker build -t ' + name + ':unstable -f ' + \
            dockerfile + ' ' + path
        env.run(command)


@task
def create_services(tag='unstable'):
    for name, _, _ in SERVICES:
        command = 'docker service create --replicas 2 ' + \
            '--name ' + name + ' --network ' + SWARM101_NETWORK + \
            ' ' + name + ':' + tag
        env.run(command)

    time.sleep(5)
    command = 'docker service update --publish-add 8000:8000 front_gateway'
    env.run(command)


@task
def setup():
    swarm_init()
    build_images()
    create_services(tag='unstable')
