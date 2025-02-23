# -*- coding: utf-8 -*-
# from odoo import http


# class GestionSalas(http.Controller):
#     @http.route('/gestion_salas/gestion_salas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_salas/gestion_salas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_salas.listing', {
#             'root': '/gestion_salas/gestion_salas',
#             'objects': http.request.env['gestion_salas.gestion_salas'].search([]),
#         })

#     @http.route('/gestion_salas/gestion_salas/objects/<model("gestion_salas.gestion_salas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_salas.object', {
#             'object': obj
#         })
