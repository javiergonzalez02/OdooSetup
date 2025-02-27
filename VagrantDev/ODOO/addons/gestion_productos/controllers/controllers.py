# -*- coding: utf-8 -*-
# from odoo import http


# class GestionProductos(http.Controller):
#     @http.route('/gestion_productos/gestion_productos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_productos/gestion_productos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_productos.listing', {
#             'root': '/gestion_productos/gestion_productos',
#             'objects': http.request.env['gestion_productos.gestion_productos'].search([]),
#         })

#     @http.route('/gestion_productos/gestion_productos/objects/<model("gestion_productos.gestion_productos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_productos.object', {
#             'object': obj
#         })
