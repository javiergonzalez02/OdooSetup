# -*- coding: utf-8 -*-

from odoo import models, fields, api  # type: ignore


class Task(models.Model):
    _name = 'final_jga.task'
    _description = 'final_jga.task'

    name = fields.Char()
    project_id = fields.Many2one(comodel_name='final_jga.project')
    employee_id = fields.Many2one(comodel_name='final_jga.employee')
    state = fields.Selection(selection=[
        ('por hacer', 'Por hacer'),
        ('en progreso', 'En progreso'),
        ('hecha', 'Hecha')
    ])
    estimated_hours = fields.Integer()
    dedicated_hours = fields.Integer()
    percent_hours = fields.Integer(compute='_get_percent_hours')

    @api.depends('percent_hours')
    def _get_percent_hours(self):
        for record in self:
            record.percent_hours = (record.dedicated_hours / record.estimated_hours) * 100

    def set_in_progress_task(self):
        self.state = 'en progreso'

    def set_done_task(self):
        self.state = 'hecha'

    def set_to_do_task(self):
        self.state = 'por hacer'