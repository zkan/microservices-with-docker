from django.http import JsonResponse


def get_current_temperature(request):
    data = {
        'celsius': 11
    }

    return JsonResponse(data)
