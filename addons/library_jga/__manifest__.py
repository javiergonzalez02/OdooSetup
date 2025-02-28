# -*- coding: utf-8 -*-
{
    'name': "Library jga",

    'summary': """
        Módulo librería JGA""",

    'description': """
        Módulo librería JGA
                   """,

    'author': "Javier González",
    'website': "https://javiergonzalez02.github.io/sge_jga/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/library_autor_views.xml',
        'views/library_libro_views.xml',
        'views/library_socio_views.xml',
        'views/library_menu_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
