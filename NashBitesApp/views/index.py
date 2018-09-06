from django.http import HttpResponse


def Welcome(request):
    return HttpResponse("Hello, world. You're at the Nash Bites App Welcome view.")