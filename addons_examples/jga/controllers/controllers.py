# -*- coding: utf-8 -*-
# from odoo import http


# class Jga(http.Controller):
#     @http.route('/jga/jga', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jga/jga/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('jga.listing', {
#             'root': '/jga/jga',
#             'objects': http.request.env['jga.jga'].search([]),
#         })

#     @http.route('/jga/jga/objects/<model("jga.jga"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jga.object', {
#             'object': obj
#         })
