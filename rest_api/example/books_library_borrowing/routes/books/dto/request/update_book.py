from marshmallow import Schema, fields

class UpdateBookRequest(Schema):
    title = fields.String()
    isbn = fields.String()
    authors = fields.List(fields.String())