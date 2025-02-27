# -*- coding: utf-8 -*-
# from odoo import http


# class LibraryJga(http.Controller):
#     @http.route('/library_jga/library_jga', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_jga/library_jga/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_jga.listing', {
#             'root': '/library_jga/library_jga',
#             'objects': http.request.env['library_jga.library_jga'].search([]),
#         })

#     @http.route('/library_jga/library_jga/objects/<model("library_jga.library_jga"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_jga.object', {
#             'object': obj
#         })
