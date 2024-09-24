from marshmallow import Schema, fields

class BookAuthor(Schema):
    name = fields.String()

class CreateBookRequest(Schema):
    title = fields.String(required=True)
    isbn = fields.String(required=True)
    authors = fields.List(fields.String(), required=True)
