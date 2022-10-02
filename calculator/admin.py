from django.contrib import admin

# Register your models here.


from .models import (
    InsuranceFee,
    InsuranceType,
    TaxType,
    SectorType,
    Calculator,
)

admin.site.register([InsuranceFee, InsuranceType, TaxType, SectorType, Calculator])
