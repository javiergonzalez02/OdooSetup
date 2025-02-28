# -*- coding: utf-8 -*-

from odoo import models, fields, api  # type: ignore


class Employee(models.Model):
    _name = 'final_jga.employee'
    _description = 'final_jga.employee'

    name = fields.Char()
    tasks_id = fields.One2many(comodel_name='final_jga.task',
        inverse_name='employee_id'
    )

    projects_id = fields.One2many(comodel_name='final_jga.project',
        inverse_name='manager_id'
    )
