# -*- coding: utf-8 -*-
# from odoo import http


# class Gestionsalas(http.Controller):
#     @http.route('/gestionsalas/gestionsalas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestionsalas/gestionsalas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestionsalas.listing', {
#             'root': '/gestionsalas/gestionsalas',
#             'objects': http.request.env['gestionsalas.gestionsalas'].search([]),
#         })

#     @http.route('/gestionsalas/gestionsalas/objects/<model("gestionsalas.gestionsalas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestionsalas.object', {
#             'object': obj
#         })
