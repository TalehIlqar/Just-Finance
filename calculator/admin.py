from django.contrib import admin

from .models import (
    InsuranceFee,
    InsuranceType,
    TaxType,
    SectorType,
    InsuranceTypeName,
    TaxTypeName
)

# Register your models here.

admin.site.register([InsuranceFee, InsuranceType, TaxType, SectorType, InsuranceTypeName, TaxTypeName])
