from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def Vendor(request):
    return HttpResponse("Hello, world. You're at the Nash Bites App vendor admin view.")