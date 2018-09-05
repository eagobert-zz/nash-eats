from django.http import HttpResponse


def vendor(request):
    return HttpResponse("Hello, world. You're at the Nash Bites App vendor view.")