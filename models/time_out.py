# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta
import datetime

class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    print("ento1")
    time_out =fields.Float(
    'Duracion Ocioso', digits=(16, 2),
    help="Duracion Tiempo Ocioso (en minutes)")    
    print("ento2")

    def _compute_timeout(self):
         for order in self:
             print("ento3")
             print(order)
             self.time_out_total = 31.55

    print("ento4")
    time_out_total = fields.Float(
    'Duracion Ocioso', digits=(16, 2),compute=_compute_timeout,
    help="Duracion Tiempo Ocioso (en minutes)")    
    
    print("ento5")



    #time_out =fields.Float(
    #    'Duracion Ocioso', digits=(16, 2),
    #    help="Duracion Tiempo Ocioso (en minutes)")    

    
class MrpWorkcenterProductivity(models.Model):
    _inherit = 'mrp.workcenter.productivity'

    time_out_total = fields.Float(
        'Duracion Ocioso', digits=(16, 2),
        help="Duracion Tiempo Ocioso (en minutes)")    

    print(time_out_total)
  
