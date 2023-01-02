# -*- coding: utf-8 -*-
{
    'name': "Streetnumber",

    'summary': """Streetnumber""",

    'description': """

    """,

    'author': "Gexi",
    'website': "https://gexi.at/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # 'depends': ['sale'],
    'depends': ['base'],
    # 'depends': ['website'],
    # 'depends': ['account'],
    # 'depends': ['stock'],
    # 'depends': ['sale_management'],
    # 'depends': ['contacts'],




    # always loaded
    'data': [
        # 'security/ir.model.access.csv',

        'views/views.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
