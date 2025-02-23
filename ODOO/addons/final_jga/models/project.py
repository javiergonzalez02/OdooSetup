# -*- coding: utf-8 -*-

from odoo import models, fields, api  # type: ignore
from odoo.exceptions import ValidationError #type: ignore

class Project(models.Model):
    _name = 'final_jga.project'
    _description = 'final_jga.project'
    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'El nombre no se puede repetir')
    ]

    name = fields.Char()
    manager_id = fields.Many2one(comodel_name='final_jga.employee')
    tasks_id = fields.One2many(comodel_name='final_jga.task',
        inverse_name='project_id'
    )
    priority = fields.Selection(selection=[
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja')
    ])
    progress = fields.Float()
    customer_id = fields.Many2one(comodel_name='res.partner')
    active = fields.Boolean(compute='_get_active_state')

    @api.depends('progress')
    def _get_active_state(self):
        for record in self:
            if record.progress == 1:
                record.active = False
            else:
                record.active = True

    @api.constrains('progress')
    def _check_progress(self):
        for record in self:
            if not (0 <= record.progress <= 1):
                raise ValidationError('El valor del progreso debe estar entre 0 y 1')

