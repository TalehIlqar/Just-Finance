from ninja import NinjaAPI

from core.api.schemas import ContactSchema
from core.models import Contact

api = NinjaAPI()


@api.post("/contact")
def contact(request, payload: ContactSchema):
    Contact.objects.create(**payload.dict())
    return {"status": "success", "message": "Contact created successfully."}
