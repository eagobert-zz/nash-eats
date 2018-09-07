from django.http import HttpResponse


def User(request):
    return HttpResponse("Hello, world. You're at the Nash Bites App user homepage view.")