# -*- coding: utf-8 -*-
{
    'name': "Gestion salas1",

    'summary': """
        Módulo para la gestión de la reserva de salas""",

    'description': """
        Módulo para la gestión de la reserva de salas
    """,

    'author': "Javier González",
    'website': "https://javiergonzalez02.github.io/sge_jga/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Management',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'security/ir.model.access.csv',
    ]
}
