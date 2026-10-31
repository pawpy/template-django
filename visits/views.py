from django.http import HttpResponse, JsonResponse

from .models import Visit


def index(request):
    # Each request records a visit, which proves the database works.
    Visit.objects.create()
    return JsonResponse({"message": "Hello from Django!", "visits": Visit.objects.count()})


def health(request):
    return HttpResponse("ok\n", content_type="text/plain")
