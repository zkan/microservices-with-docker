import requests

from django.http import HttpResponse


def index(request):
    html = 'Let\'s see the temperature today: '

    response = requests.get('http://bangkok:8000/')
    data = response.json()
    html += 'bangkok: ' + str(data['celsius'])

    response = requests.get('http://tokyo:3000/')
    data = response.json()
    html += ', tokyo: ' + str(data['celsius'])

    response = requests.get('http://munich:8000/')
    data = response.json()
    html += ', munich: ' + str(data['celsius'])

    return HttpResponse(html)
