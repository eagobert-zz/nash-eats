from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


@login_required
class VendorView(TemplateView):
    template_name = 'vendor.html'