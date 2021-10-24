# -*- coding: utf-8 -*-
{
    'name': "BETTA MRP TIME",

    'summary': """
        Agrega boton qeu cuenta el Tiempo Muerto en los
        proyectos de Fabricacion""",

    'description': """
        Control Tiempo muerto 
    """,

    'author': "Betta ERP",
    'website': "http://www.bettaerp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing/Manufacturing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mrp','base',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/time_out.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
