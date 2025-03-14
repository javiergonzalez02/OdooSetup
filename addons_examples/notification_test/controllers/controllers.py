# -*- coding: utf-8 -*-
# from odoo import http


# class TestMessage(http.Controller):
#     @http.route('/test_message/test_message', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_message/test_message/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_message.listing', {
#             'root': '/test_message/test_message',
#             'objects': http.request.env['test_message.test_message'].search([]),
#         })

#     @http.route('/test_message/test_message/objects/<model("test_message.test_message"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_message.object', {
#             'object': obj
#         })
