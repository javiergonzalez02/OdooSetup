# -*- coding: utf-8 -*-
from sqlite3 import Date

from odoo import models, fields, api  # type: ignore

class warranty(models.Model):
    _name = 'jga.warranty'
    _description = 'jga.warranty'
    _sql_constraints= [
        ('unique_name', 'unique(name)', 'El nombre debe se único')
    ]

    name = fields.Char()
    claims = fields.One2many(comodel_name='jga.claim', inverse_name='warranty_id')
    product_id = fields.Many2one('jga.product')
    customer_id = fields.Many2one('res.partner')
    warranty_code = fields.Integer(required=True)
    start_date = fields.Date(compute='_fecha_actual')
    end_date = fields.Date()
    warranty_type = fields.Selection(selection=[('fabricante', 'Fabricante'), ('distribuidor', 'Distribuidor'),
                                                ('ampliada', 'Ampliada')])
    status = fields.Selection(selection=[('activada', 'Activada'), ('expirada', 'Expirada'),
                                                ('anulada', 'Anulada')])

    @api.depends()
    def _fecha_actual(self):
        for record in self:
            record.start_date = Date.today()

    @api.depends()
    def _fecha_final(self):
        for record in self:
            if record.status=='anulada':
                record.end_date=fields.Date(readOnly=True)

