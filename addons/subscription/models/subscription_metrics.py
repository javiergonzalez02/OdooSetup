# -*- coding: utf-8 -*-
from odoo import models, fields, api  # type: ignore

class SubscriptionMetrics(models.Model):
    _name = 'subscription.subscription_metrics'
    _description = 'Métricas de Suscripciones'

    # 1. Fecha
    date = fields.Date(
        string="Fecha",
        default=fields.Date.today
    )
    # 2. Número de suscripciones activas
    active_subscriptions = fields.Integer(
        string="Número de Suscripciones Activas"
    )
    # 3. Ingresos generados
    generated_revenue = fields.Float(
        string="Ingresos Generados",
        digits=(12, 2)
    )
    # 4. Tasa de renovación
    renewal_rate = fields.Float(
        string="Tasa de Renovación",
        compute="_compute_rates",
        digits=(12, 2),
        help="(Renovaciones / Suscripciones Activas) * 100"
    )
    # 5. Tasa de cancelación
    cancellation_rate = fields.Float(
        string="Tasa de Cancelación",
        compute="_compute_rates",
        digits=(12, 2),
        help="(Cancelaciones / Suscripciones Activas) * 100"
    )
    # 6. Renovaciones
    renewals = fields.Integer(
        string="Renovaciones"
    )
    # 7. Nuevas suscripciones
    new_subscriptions = fields.Integer(
        string="Nuevas Suscripciones"
    )
    # 8. Suscripciones canceladas
    cancelled_subscriptions = fields.Integer(
        string="Suscripciones Canceladas"
    )
    # 9. Clientes recurrentes y Nuevos clientes
    recurring_customers = fields.Integer(
        string="Clientes Recurrentes"
    )
    new_customers = fields.Integer(
        string="Nuevos Clientes"
    )
    # 10. Ingresos promedio por usuario
    arpu = fields.Float(
        string="Ingresos Promedio por Usuario (ARPU)",
        compute="_compute_arpu",
        digits=(12, 2)
    )
    # 11. Tasa de conversión
    conversion_rate = fields.Float(
        string="Tasa de Conversión"
    )
    # 12. Churn Rate
    churn_rate = fields.Float(
        string="Churn Rate (Tasa de Pérdida de Clientes)"
    )
    # 13. Lifetime Value (LTV)
    ltv = fields.Float(
        string="Lifetime Value (LTV)",
        digits=(12, 2)
    )
    # 14. Costo de adquisición de clientes
    cac = fields.Float(
        string="Costo de Adquisición de Clientes (CAC)",
        digits=(12, 2)
    )
    # 15. Notas
    notes = fields.Text(
        string="Notas"
    )
    # 16. Relación con el Modelo de Suscripciones
    subscription_ids = fields.One2many(
        comodel_name='subscription.subscription',
        inverse_name='metric_id',
        string="Suscripciones Relacionadas"
    )

    @api.depends('active_subscriptions', 'renewals', 'cancelled_subscriptions')
    def _compute_rates(self):
        for rec in self:
            if rec.active_subscriptions:
                rec.renewal_rate = (rec.renewals / rec.active_subscriptions) * 100
                rec.cancellation_rate = (rec.cancelled_subscriptions / rec.active_subscriptions) * 100
            else:
                rec.renewal_rate = 0.0
                rec.cancellation_rate = 0.0

    @api.depends('active_subscriptions', 'generated_revenue')
    def _compute_arpu(self):
        for rec in self:
            if rec.active_subscriptions:
                rec.arpu = rec.generated_revenue / rec.active_subscriptions
            else:
                rec.arpu = 0.0
