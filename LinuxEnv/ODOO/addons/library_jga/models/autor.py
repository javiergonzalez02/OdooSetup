# -*- coding: utf-8 -*-

from odoo import models, fields, api  # type: ignore

class Autor(models.Model):
    _name = 'library_jga.autor'
    _description = 'Autor de Libros'

    name = fields.Char(string='Nombre', required=True)
    country_id = fields.Many2one('res.country', string='País de Origen', required=True)
    libro_ids = fields.One2many('library_jga.libro', 'autor_id', string='Libros Escritos')
