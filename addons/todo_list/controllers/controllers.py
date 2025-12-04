# -*- coding: utf-8 -*-
# from odoo import http


# class KanbaApp(http.Controller):
#     @http.route('/kanba_app/kanba_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kanba_app/kanba_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kanba_app.listing', {
#             'root': '/kanba_app/kanba_app',
#             'objects': http.request.env['kanba_app.kanba_app'].search([]),
#         })

#     @http.route('/kanba_app/kanba_app/objects/<model("kanba_app.kanba_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kanba_app.object', {
#             'object': obj
#         })

