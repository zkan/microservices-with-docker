from fabric.api import (
    local,
    settings,
    task
)
from fabric.state import env


SWARM101_NETWORK = 'swarm101'


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
    services = [
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
            'gateway',
            'gateway/Dockerfile',
            'gateway'
        ),
    ]
    for name, dockerfile, path in services:
        command = 'docker build -t ' + name + ':unstable -f ' + \
            dockerfile + ' ' + path
        env.run(command)


@task
def create_services(tag='unstable'):
    services = [
        'bangkok',
        'munich',
        'tokyo',
        'nyc',
    ]
    for service in services:
        command = 'docker service create --name ' + \
            service + ' --network ' + SWARM101_NETWORK + \
            ' ' + service + ':' + tag
        env.run(command)

    service = 'gateway'
    command = 'docker service create --name ' + \
        service + ' --network ' + SWARM101_NETWORK + \
        ' -p 8000:8000 ' + service + ':' + tag
    env.run(command)


@task
def setup():
    swarm_init()
    build_images()
    create_services(tag='unstable')
