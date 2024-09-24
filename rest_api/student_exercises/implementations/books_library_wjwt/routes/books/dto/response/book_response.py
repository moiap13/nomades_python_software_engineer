from marshmallow import Schema, fields

class BookResponseList(Schema):
    id = fields.String()
    title = fields.String()
    isbn = fields.String()
    authors = fields.List(fields.String())

class BookResponse(Schema):
    id = fields.String()
    title = fields.String()
    isbn = fields.String()
    authors = fields.List(fields.String())

class BookId(Schema):
    id = fields.String()

class BookISBN(Schema):
    isbn = fields.String()