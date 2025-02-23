# -*- coding: utf-8 -*-

from odoo import models, fields, api # type: ignore


class gestion_productos(models.Model):
    _name = 'gestion_productos.gestion_productos'
    _description = 'gestion_productos.gestion_productos'

    # Información básica
    nombre = fields.Char()
    descripcion = fields.Text()
    codigo = fields.Char(required=True)
    imagen = fields.Binary()

    # Categoría y tipo
    categoria = fields.Selection(
        selection=[
            ('Jardín', 'Jardín'),
            ('Hogar', 'Hogar'),
            ('Electrodomésticos', 'Electrodomésticos')
        ],
        required=True,
        default='Jardín'
    )
    tipo = fields.Boolean(string="Destacable")

    # Información económica
    precio = fields.Float()
    stock = fields.Integer()

    # Fecha y disponibilidad
    fecha_creacion = fields.Date(
        default=fields.Date.today,
        readonly=True,
        string="Fecha de Creación"
    )
    fecha_actualizacion = fields.Date(
        default=fields.Date.today,
        readonly=True,
        string="Fecha de Actualización"
    )

    # Información adicional
    activo = fields.Boolean(string="Activo", default=True)
    peso = fields.Float(digits=(16, 2))
