import email
from ninja import Schema


class ContactSchema(Schema):
    name: str
    email: str
    subject: str
