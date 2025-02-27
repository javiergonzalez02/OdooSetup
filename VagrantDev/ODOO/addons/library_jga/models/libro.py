
from odoo import models, fields  # type: ignore

class Libro(models.Model):
    _name = 'library_jga.libro'
    _description = 'Libro de la Biblioteca'

    name = fields.Char(string='Título', required=True)
    autor_id = fields.Many2one('library_jga.autor', string='Autor', required=True)
    genero = fields.Selection([
        ('novela', 'Novela'),
        ('drama', 'Drama'),
        ('ciencia_ficcion', 'Ciencia Ficción'),
        ('misterio', 'Misterio'),
        ('terror', 'Terror'),
        ('historico', 'Histórico'),
    ], string='Género', required=True)
    socio_ids = fields.Many2many('library_jga.socio', string='Socios que han Prestado')
