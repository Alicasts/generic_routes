from django.http import JsonResponse

def handleRequest(request, routeParameter = None):
    return JsonResponse({"message": f"{routeParameter}"})
