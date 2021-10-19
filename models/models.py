# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /opt/odoo/sources/betta_mrp_time_out(models.Model):
#     _name = '/opt/odoo/sources/betta_mrp_time_out./opt/odoo/sources/betta_mrp_time_out'
#     _description = '/opt/odoo/sources/betta_mrp_time_out./opt/odoo/sources/betta_mrp_time_out'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
