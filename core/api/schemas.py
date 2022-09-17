from ninja import Schema


class ContactSchema(Schema):
    name: str
    number: str
    subject: str
