# -*- coding: utf-8 -*-

from odoo import models, fields, api #type: ignore


class Warranty(models.Model):
    _name = 'ing.warranty'
    _description = 'Gestión de garantías'
    _sql_constraints = [
            ('unique_warranty_code', 'unique(warranty_code)', 'El codigo de garantia no se puede repetir'),
            ('max_warranty_code_length', 'CHECK(length(warranty_code) = 5)', 'La garantia solo puede tener cinco caracteres')
            ]
    

    name = fields.Char()
    product_id = fields.Many2one(
            comodel_name='ing.product'
            )
    customer_id = fields.Many2one(
            comodel_name='res.partner'
            )
    warranty_code = fields.Char( required = True )
    start_date = fields.Date(compute='_get_today_date')
    end_date = fields.Date()
    warranty_type = fields.Selection(selection=[
    ('fabricante', 'Fabricante'),
    ('distribuidor', 'Distribuidor'),
    ('ampliada', 'Ampliada'),
    ]) 
 
    status = fields.Selection(selection=[
    ('activa', 'Activa'),
    ('expirada', 'Expirada'),
    ('anulada', 'Anulada'),
    ]) 

    @api.depends('start_date')
    def _get_today_date(self):
        for record in self:
            record.start_date = fields.Date.today()
