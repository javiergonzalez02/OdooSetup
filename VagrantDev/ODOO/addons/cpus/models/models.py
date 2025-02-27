# -*- coding: utf-8 -*-

from odoo import models, fields, api  # type: ignore

class cpu(models.Model):
    # nombre modulo y modelo
    _name = 'cpus.cpu'
    _description = 'cpus.cpu'

    name = fields.Char()
    manufacturer = fields.Char()
    total_cores = fields.Integer()
    p_cores = fields.Integer()
    e_cores = fields.Integer()
    base_frequency = fields.Float()
    max_frequency = fields.Float()
