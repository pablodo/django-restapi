from django.http import HttpResponse


def movies(request):
    return HttpResponse("Movies list not implemented yet", status=501)
