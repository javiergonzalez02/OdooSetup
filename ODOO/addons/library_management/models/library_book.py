from odoo import models, fields, api # type: ignore


class library_book(models.Model):
    _name = 'library_management.library_book'
    _description = 'library_management.library_book'

    nombre_libro = fields.Text()
    autor = fields.Char()
    fecha_publicacion = fields.Date()
    isbn = fields.Integer()
    sinopsis = fields.Text()