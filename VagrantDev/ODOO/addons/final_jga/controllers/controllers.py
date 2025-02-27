# -*- coding: utf-8 -*-
from odoo import http  # type: ignore
from odoo.http import request, Response  # type: ignore


class FinalJga(http.Controller):
    @http.route('/jga/web/', auth='public', type='http', website=True)
    def index(self, **kw):
        tasks = request.env['final_jga.task'].sudo().search([])
        return request.render('final_jga.jga_message_web', {
            'tasks': tasks
        })
