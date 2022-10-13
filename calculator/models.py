from django.db import models

# Create your models here.


class InsuranceFee(models.Model):
    from_number = models.IntegerField()
    to_number = models.IntegerField()
    from_to_formula = models.CharField(max_length=255, blank=True, null=True)
    to_from_formula = models.CharField(max_length=255, blank=True, null=True)
    insurance_type = models.ForeignKey(
        "InsuranceType", on_delete=models.CASCADE, related_name="fees", blank=True, null=True
    )

    def __str__(self):
        return f"{self.from_number} - {self.to_number} - {self.insurance_type.name}"


class InsuranceType(models.Model):
    """
        Sığortaolunan,
        Sığortaedən
    """
    name = models.CharField(max_length=255, blank=True, null=True)
    tax_type = models.ForeignKey("TaxType", on_delete=models.CASCADE, related_name="insurance_types", blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.tax_type.name}"

    class Meta:
        verbose_name = "Insurance Type"
        verbose_name_plural = "Insurance Types"


class TaxType(models.Model):
    """
        Gəlir vergisi,
        Sosial sığorta haqqı,
        İşsizlikdən sığorta haqqı,
        İcbari tibbi sığorta
    """
    sector_type = models.ForeignKey("SectorType", on_delete=models.CASCADE, related_name="tax_types", blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.sector_type.name}"


class SectorType(models.Model):
    """
        Neft-qaz sahəsində fəaliyyəti olmayan və qeyri-dövlət sektoruna aid edilən,
        Neft-qaz sahəsində fəaliyyəti olan və dövlət sektoruna aid edilən
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
