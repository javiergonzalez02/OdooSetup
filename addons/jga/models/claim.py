# -*- coding: utf-8 -*-

from odoo import models, fields, api  # type: ignore


class claim(models.Model):
    _name = 'jga.claim'
    _description = 'jga.claim'

    name = fields.Char(unique=True)
    description = fields.Text()
    status = fields.Selection(selection=[('abierta', 'Abierta'), ('en_proceso', 'En proceso'), ('resuelta', 'Resuelta'),
                                         ('cerrada', 'Cerrada')])
    res_date = fields.Date()
    warranty_id = fields.Many2one('jga.warranty')

    def resolver(self):
        if self.status == 'abierta':
            claim.status = 'resuelta'
        if self.status == 'resuelta':
            claim.status = 'abierta'
        if self.status == 'cerrada':
            claim.status = 'abierta'
