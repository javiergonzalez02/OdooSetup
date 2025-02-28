# -*- coding: utf-8 -*-
from odoo import models, fields, api #type: ignore
from odoo.exceptions import ValidationError #type: ignore


class Claim(models.Model):
    _name = 'ing.claim'
    _description = 'Gestion de las reclamaciones'

    name = fields.Char()
    description = fields.Char()
    status = fields.Selection(selection=[
    ('abierta', 'Abierta'),
    ('en_proceso', 'En proceso'),
    ('resuelta', 'Resuelta'),
    ('cerrada', 'Cerrada')
    ]) 
    res_date = fields.Date() 
    warranty_id = fields.Many2one(comodel_name='ing.warranty')

    @api.constrains('description')
    def _check_name(self):
        for record in self:
            if not record.description or len(record.description) < 20:
                raise ValidationError('La descripcion tiene que tener por lo menos 20 caracteres')

    def resolve_claim(self):
        self.status = 'resuelta'

    def unresolve_claim(self):
        self.status = 'abierta'

