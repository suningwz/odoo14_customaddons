# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Sendo Integration',
    'version': '1.1',
    'summary': '',
    'sequence': 10,
    'description': """
    Sendo Integration with API by Python Http Request
    """,
    'category': 'Uncategorized',
    'website': '#',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/cron_job_sendo.xml',
        'wizard/connect_shop_wizard.xml',
        'views/sendo_seller_product_view.xml',
        'views/sendo_list_order_view.xml',
        'views/sendo_categories_view.xml',
        'views/sendo_seller_view.xml',
        # 'views/assets_backend.xml',
    ],
    'demo': [
    ],
     #  'qweb': [
     #      'static/src/xml/template.xml',
     # ],
    'installable': True,
    'application': True,
    'auto_install': False,
}