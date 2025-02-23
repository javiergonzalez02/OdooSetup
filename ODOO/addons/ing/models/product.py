# -*- coding: utf-8 -*-

from odoo import models, fields, api #type: ignore


class Product(models.Model):
    _name = 'ing.product'
    _description = 'Manejo de productos'

    name = fields.Char()
    warranties = fields.One2many(
            comodel_name='ing.warranty',
            inverse_name = 'product_id'
            )
