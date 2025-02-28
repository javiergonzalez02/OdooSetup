# -*- coding: utf-8 -*-
from odoo import http #type: ignore
from odoo.http import request, Response #type: ignore
import json

class Ing(http.Controller):
    @http.route("/api/warranty/<string:code>", type="http", methods=['GET'], csrf=False)
    def api_warranties(self, code):
        try:
            warranties = request.env['ing.warranty'].sudo().search([('warranty_code', '=', code)], limit = 1)
            if len(warranties) == 0:
                return Response(
                        json.dumps({
                            "error": 404,
                            "desc": "El codigo introducido no corresponde con ningun registro"
                            }),
                        content_type = 'application/json',
                        status = 404
                        )
            response = []
            for war in warranties:
                response.append({
                    "name": war.name,
                    "status": war.status if war.status else "no_seleccionado"
                    })
            return Response(
                    json.dumps(response),
                    content_type = 'application/json',
                    status = 200
                    )
        except Exception as e:
            return Response(
                    json.dumps({
                        "error":500,
                        "desc": f"Ocurrio un error interno del servidor: {str(e)}"}),
                    content_type = 'application/json',
                    status = 500
                    )

