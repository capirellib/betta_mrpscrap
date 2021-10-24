# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta
import datetime



class MrpWorkorder(models.Model):
    
    _inherit = 'mrp.workorder'

    time_out =fields.Float(
    'Duracion Ocioso', digits=(16, 2) ,
    help="Duracion Tiempo Ocioso (en minutes)")
    
    show_ocio = fields.Integer(default=1)
    
    print("********************************")
    print(show_ocio)
    print("********************************")


    def _compute_timeout(self):
         for order in self:
             print("ento3")
             print(order)
             self.time_out_total = 31.55


    time_out_total = fields.Float(
    'Ocioso Total', digits=(16, 2), compute=_compute_timeout,
    help="Total Tiempo Ocioso (en minutes)")    


    def button_start(self):
        self.show_ocioso = True
        return super().button_start()

#*********************************************************************************
#*********************************************************************************



    #time_out =fields.Float(
    #    'Duracion Ocioso', digits=(16, 2),
    #    help="Duracion Tiempo Ocioso (en minutes)")    

    
class MrpWorkcenterProductivity(models.Model):
    _inherit = 'mrp.workcenter.productivity'

    time_out_total = fields.Float(
        'Ocioso Total', digits=(16, 2),
        help="Duracion Tiempo Ocioso (en minutes)")    

    
    print(time_out_total)
  





# class MrpWorkorder(models.Model):
#     _inherit = 'mrp.workorder'

#     #def _compute_time_out(self):
#     #    print("seleccion de tiempo ociosa")    
#     #    self.time_out = 60.8    
        
    
#     time_out =fields.Float(
#         'Duracion Ocioso', digits=(16, 2),
#         help="Duracion Tiempo Ocioso (en minutes)")    


