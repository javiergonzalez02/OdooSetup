from odoo import models, fields  # type: ignore

class Socio(models.Model):
    _name = 'library_jga.socio'
    _description = 'Socio de la Biblioteca'

    name = fields.Char(string='Nombre', required=True)
    phone = fields.Char(string='Teléfono')
    libro_ids = fields.Many2many('library_jga.libro', string='Libros Prestados')
