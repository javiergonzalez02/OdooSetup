# -*- coding: utf-8 -*-

from odoo import models, fields, api # type: ignore


class product(models.Model):
    _name = 'jga.product'
    _description = 'jga.product'

    name = fields.Char()
    warranties = fields.One2many('jga.warranty', 'product_id')
