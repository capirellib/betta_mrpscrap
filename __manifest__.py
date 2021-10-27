# -*- coding: utf-8 -*-
{
    'name': "MRP Betta Tiempo Ocioso",

    'summary': """
        Agrega Control en que los Operarios realizan otras tares indirectas al 
        proceso de Fabricacion (Incremento en el costo del Proyecto)""",

    'description': """
        Control Tiempo Ocioso  
    """,

    'author': "Betta ERP - (Carlos E. Pirelli)",
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
        
        'views/views.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],

    'images': [
        'static/description/icon.png',
],

}
