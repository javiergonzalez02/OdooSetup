# -*- coding: utf-8 -*-
from itertools import count

from odoo import models, fields, api, exceptions


class gestion_salas(models.Model):
    _name = 'gestion_salass.gestion_salas'
    _description = 'gestion_salass.gestion_salas'

    nombre_sala = fields.Selection(
        selection=[
            ('comedorPequeño', 'Comedor Pequeño'),
            ('comedorAuxiliar', 'Comedor Auxiliar'),
            ('comedorPrincipal', 'Comedor Principal'),
            ('comedorPrivado', 'Comedor Privado')
        ],
        string="Elige un comedor",
        required=True,
        default='comedorAuxiliar'
    )
    nombre_cliente = fields.Text()
    numero_personas = fields.Integer()
    fecha_reserva = fields.Date()
    celiaco = fields.Boolean()
    comentarios = fields.Text()

    @api.model
    def create(self, vals):
        if 'nombre_sala' in vals and 'fecha_reserva' in vals:
            records = self.search([('nombre_sala', '=', vals['nombre_sala']), ('fecha_reserva', '=', vals['fecha_reserva'])])
            count_total_personas = 0
            for record in records:
                count_total_personas += record['numero_personas']
            if count_total_personas > self.capacidad_salas(vals['nombre_sala']):
                raise exceptions.ValidationError("La sala ya está completa para esta fecha.")
            numero_personas_n = vals.get('numero_personas')
            if (numero_personas_n + count_total_personas) > self.capacidad_salas(vals['nombre_sala']):
                raise exceptions.ValidationError("El número de personas excede la capacidad de la sala.")
        return super(models.Model, self).create(vals)

    def capacidad_salas(self, sala):
        if sala == 'comedorPequeño':
            return 15
        elif sala == 'comedorAuxiliar':
            return 20
        elif sala == 'comedorPrincipal':
            return 50
        elif sala == 'comedorPrivado':
            return 10
