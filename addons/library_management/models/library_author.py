from odoo import models, fields, api # type: ignore


class library_author(models.Model):
    _name = 'library_management.library_author'
    _description = 'library_management.library_author'

    nombre_autor = fields.Text()
    fecha_nacimiento = fields.Date()
    biografia = fields.Text()
    libros = fields.Text()