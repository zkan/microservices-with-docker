import requests

from django.shortcuts import render


def index(request):
    context = {}

    response = requests.get('http://bangkok:8000/')
    data = response.json()
    context['bangkok'] = data['celsius']

    response = requests.get('http://tokyo:3000/')
    data = response.json()
    context['tokyo'] = data['celsius']

    response = requests.get('http://munich:8000/')
    data = response.json()
    context['munich'] = data['celsius']

    return render(
        request,
        'index.html',
        context
    )
