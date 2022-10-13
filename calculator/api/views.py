from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from django.utils.translation import gettext_lazy as _

from calculator.models import SectorType


class CalculatorView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        try:
            sector_type = SectorType.objects.get(id=request.data["sector_type"])
        except SectorType.DoesNotExist:
            return Response(
                {"error": _("Sector type does not exist.")},
                status=status.HTTP_400_BAD_REQUEST,
            )
        from_number = request.data.get("from_number")
        to_number = request.data.get("to_number")

        return Response(
            {
                "sector_type": {
                    "id": sector_type.id,
                    "name": sector_type.name,
                    "tax_types": [
                        {
                            "id": tax_type.id,
                            "name": tax_type.name,
                            "insurance_types": [
                                {
                                    "id": insurance_type.id,
                                    "name": insurance_type.name,
                                    "fee": {
                                            "from_number": insurance_type.fees.filter(from_number__lte=from_number).order_by("-from_number").first().from_number if insurance_type.fees.filter(from_number__lte=from_number).order_by("-from_number").first() else None,
                                            "to_number": insurance_type.fees.filter(from_number__lte=from_number).order_by("-from_number").first().to_number if insurance_type.fees.filter(from_number__lte=from_number).order_by("-from_number").first() else None,
                                            "fee": eval(insurance_type.fees.filter(from_number__lte=from_number).order_by("-from_number").first().from_to_formula, {}, {"x": from_number}) if insurance_type.fees.filter(from_number__lte=from_number).order_by("-from_number").first() else None,
                                        },
                                }
                                for insurance_type in tax_type.insurance_types.all()
                            ],
                        }
                        for tax_type in sector_type.tax_types.all()
                    ],
                }
            }
        )
