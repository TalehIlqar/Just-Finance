from django.db import models

# Create your models here.


class InsuranceFee(models.Model):
    from_number = models.IntegerField()
    to_number = models.IntegerField()
    from_to_formula = models.CharField(max_length=255, blank=True, null=True)
    to_from_formula = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.from_number} - {self.to_number}"


class InsuranceTypeName(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class InsuranceType(models.Model):
    """
        Sığortaolunan,
        Sığortaedən
    """
    name = models.ForeignKey(InsuranceTypeName, on_delete=models.CASCADE)
    fees = models.ManyToManyField(InsuranceFee, verbose_name="Fees")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Insurance Type"
        verbose_name_plural = "Insurance Types"


class TaxTypeName(models.Model):
    """
        Vergi adı
    """
    name = models.CharField(max_length=255, verbose_name="Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tax Type Name"
        verbose_name_plural = "Tax Type Names"


class TaxType(models.Model):
    """
        Gəlir vergisi,
        Sosial sığorta haqqı,
        İşsizlikdən sığorta haqqı,
        İcbari tibbi sığorta
    """
    name = models.ForeignKey(TaxTypeName, on_delete=models.CASCADE, verbose_name="Name")
    insurance_types = models.ManyToManyField(
        InsuranceType, verbose_name="Insurance Types"
    )

    def __str__(self):
        return self.name


class SectorType(models.Model):
    """
        Neft-qaz sahəsində fəaliyyəti olmayan və qeyri-dövlət sektoruna aid edilən,
        Neft-qaz sahəsində fəaliyyəti olan və dövlət sektoruna aid edilən
    """
    name = models.CharField(max_length=100)
    tax_types = models.ManyToManyField(TaxType, related_name="sector_types")

    def __str__(self):
        return self.name
