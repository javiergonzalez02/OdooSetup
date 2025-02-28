# -*- coding: utf-8 -*-
import datetime
from datetime import timedelta

from odoo import models, fields, api  # type: ignore


class Subscription(models.Model):
    _name = 'subscription.subscription'
    _description = 'Gestión de Suscripciones'

    # Campos básicos
    name = fields.Char()
    customer_id = fields.Many2one('res.partner')
    subscription_code = fields.Char()
    start_date = fields.Date()
    end_date = fields.Date()
    duration_months = fields.Integer()
    renewal_date = fields.Date()
    status = fields.Selection(selection=[('active', 'Activa'), ('expired', 'Expirada'), ('pending', 'Pendiente'), (
        'cancelled', 'Cancelada')])
    is_renewable = fields.Boolean(default=False)
    auto_renewal = fields.Boolean(default=False)
    price = fields.Float(string="Precio")
    metric_id = fields.Many2one(
        comodel_name='subscription.subscription_metrics',
        string="Métricas"
    )

    # Campos de uso
    usage_limit = fields.Integer()
    current_usage = fields.Integer()
    use_percent = fields.Float(compute='_compute_use_percent')

    @api.depends('current_usage', 'usage_limit')
    def _compute_use_percent(self):
        for record in self:
            if record.usage_limit:
                record.use_percent = (record.current_usage / record.usage_limit) * 100
            else:
                record.use_percent = 0.0

    def action_add_15_days(self):
        self.end_date = self.end_date + datetime.timedelta(days=15)