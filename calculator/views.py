from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from calculator.models import SectorType, InsuranceType


# Create your views here.


def calculator(request):
    context = {
        "title": _("Calculator"),
        "sector_types": SectorType.objects.all(),
        "insurance_type_names": [insurance_type[0] for insurance_type in sorted(InsuranceType.NAME_CHOICES, key=lambda x: x[1])],
    }
    return render(request, "pages/calculator.html", context)
