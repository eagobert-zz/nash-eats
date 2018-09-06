from django.http import HttpResponse


def Vendor(request):
    return HttpResponse("Hello, world. You're at the Nash Bites App vendor admin view.")