from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from calculator.models import SectorType


class CalculatorView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        sector_type = get_object_or_404(SectorType, id=request.data.get("sector_type"))
        from_number = request.data.get("from_number")
        to_number = request.data.get("to_number")

        if from_number:
            qs_filter = {
                "from_number__lte": from_number,
                "to_number__gt": from_number,
                "from_to_formula__isnull": False,
            }
        elif to_number:
            qs_filter = {
                "from_number__lte": to_number,
                "to_number__gt": to_number,
                "to_from_formula__isnull": False,
            }
        else:
            return Response(
                {"error": _("Please provide from_number or to_number")},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = []
        for tax_type in sector_type.tax_types.all():
            for insurance_type in tax_type.insurance_types.all():
                insurance_fees = insurance_type.fees.filter(**qs_filter).order_by("insurance_type__name")
                for insurance_fee in insurance_fees:
                    data.append(
                        {
                            "tax_type": tax_type.name,
                            "fee": round(eval(insurance_fee.from_to_formula or insurance_fee.to_from_formula, {}, {'x': from_number or to_number})),
                        }
                    )
        return Response(data, status=status.HTTP_200_OK)
