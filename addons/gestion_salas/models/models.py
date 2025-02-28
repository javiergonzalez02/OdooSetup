# -*- coding: utf-8 -*-

from odoo import models, fields, api  # type: ignore


class gestion_salas(models.Model):
    _name = 'gestion_salas.gestion_salas'
    _description = 'gestion_salas.gestion_salas'

    nombre_sala = fields.Char()
    capacidad = fields.Integer()
    fecha_reserva = fields.Date()
    reservada = fields.Boolean()
    comentarios = fields.Text()

