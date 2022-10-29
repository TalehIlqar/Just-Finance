# from django.contrib import admin

# from .models import (
#     InsuranceFee,
#     InsuranceType,
#     TaxType,
#     SectorType,
# )

# # Register your models here.


# class InsuranceFeeInline(admin.TabularInline):
#     model = InsuranceFee
#     extra = 0


# class InsuranceTypeInline(admin.TabularInline):
#     model = InsuranceType
#     extra = 0
#     inlines = [InsuranceFeeInline]


# class TaxTypeInline(admin.TabularInline):
#     model = TaxType
#     extra = 0
#     inlines = [InsuranceTypeInline]


# class TaxTypeAdmin(admin.ModelAdmin):
#     inlines = [InsuranceTypeInline]


# class SectorTypeAdmin(admin.ModelAdmin):
#     inlines = [TaxTypeInline]


# class InsuranceTypeAdmin(admin.ModelAdmin):
#     inlines = [InsuranceFeeInline]


# admin.site.register(SectorType, SectorTypeAdmin)
# admin.site.register(TaxType, TaxTypeAdmin)
# admin.site.register(InsuranceType, InsuranceTypeAdmin)
