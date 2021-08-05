# -*- coding: utf-8 -*-
{
    'name': "academy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Marketing',
    'version': '0.1',
    'sequence': -99,

    # any module necessary for this one to work correctly
    'depends': ['website', 'account', 'base', 'mail','contacts','website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/search.xml',
        'views/data.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
