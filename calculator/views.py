from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from calculator.models import SectorType


# Create your views here.


def calculator(request):
    context = {
        "title": _("Calculator"),
        "sector_types": SectorType.objects.all(),
    }
    return render(request, "pages/calculator.html", context)
