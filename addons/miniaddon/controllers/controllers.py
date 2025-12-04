# -*- coding: utf-8 -*-
# from odoo import http


# class Miniaddon(http.Controller):
#     @http.route('/miniaddon/miniaddon', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/miniaddon/miniaddon/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('miniaddon.listing', {
#             'root': '/miniaddon/miniaddon',
#             'objects': http.request.env['miniaddon.miniaddon'].search([]),
#         })

#     @http.route('/miniaddon/miniaddon/objects/<model("miniaddon.miniaddon"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('miniaddon.object', {
#             'object': obj
#         })

