from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import (
    InsuranceFee,
    InsuranceType,
    TaxType,
    SectorType,
    Calculator,
)


class InsuranceFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceFee
        fields = "__all__"


class InsuranceTypeSerializer(serializers.ModelSerializer):
    fees = InsuranceFeeSerializer(many=True, read_only=True)

    class Meta:
        model = InsuranceType
        fields = "__all__"


class TaxTypeSerializer(serializers.ModelSerializer):
    insurance_types = InsuranceTypeSerializer(many=True, read_only=True)

    class Meta:
        model = TaxType
        fields = "__all__"


class SectorTypeSerializer(serializers.ModelSerializer):
    tax_types = TaxTypeSerializer(many=True, read_only=True)

    class Meta:
        model = SectorType
        fields = "__all__"


class CalculatorSerializer(serializers.ModelSerializer):
    sector_type = SectorTypeSerializer(read_only=True)

    class Meta:
        model = Calculator
        fields = "__all__"
