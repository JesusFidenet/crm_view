# -*- coding: utf-8 -*-
# from odoo import http


# class CrmView(http.Controller):
#     @http.route('/crm_view/crm_view/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_view/crm_view/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_view.listing', {
#             'root': '/crm_view/crm_view',
#             'objects': http.request.env['crm_view.crm_view'].search([]),
#         })

#     @http.route('/crm_view/crm_view/objects/<model("crm_view.crm_view"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_view.object', {
#             'object': obj
#         })
