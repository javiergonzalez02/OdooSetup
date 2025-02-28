# -*- coding: utf-8 -*-
# from odoo import http


# class Cpus(http.Controller):
#     @http.route('/cpus/cpus', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cpus/cpus/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cpus.listing', {
#             'root': '/cpus/cpus',
#             'objects': http.request.env['cpus.cpus'].search([]),
#         })

#     @http.route('/cpus/cpus/objects/<model("cpus.cpus"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cpus.object', {
#             'object': obj
#         })
