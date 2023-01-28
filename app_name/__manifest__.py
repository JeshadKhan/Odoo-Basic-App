# -*- coding: utf-8 -*-
{
    'name': 'App Name',
    'summary': """Something about the App.""",
    'description': """
App Name
========
Something about the App.
    """,
    'version': '15.0.1.0',
    'author': 'Company Name',
    'website': 'http://www.company.com',
    'category': 'Tools',
    'sequence': 1,
    'depends': [
        'base',
        'web',
    ],
    'data': [
        ## Data
        'data/ir_sequence.xml',

        ## Security
        'security/ir.model.access.csv',

        ## Report
        'reports/report_paper_format.xml',
        'reports/my_model_name_report.xml',
        
        ## Wizard
        'wizards/my_model_name_wizard.xml',
        
        ## View
        'views/my_model_name_view.xml',
        'views/menus.xml',
    ],
    'qweb': [
        ## Template
        'static/src/xml/*.xml',
    ],
    'assets': {
        'web.assets_backend': [
            ('include', 'app_name/static/src/css/web_assets_backend.css'),
            ('include', 'app_name/static/src/js/web_assets_backend.js'),
        ],
        'web.assets_frontend': [
            ('include', 'app_name/static/src/css/web_assets_frontend.css'),
            ('include', 'app_name/static/src/js/web_assets_frontend.js'),
        ],
        'web.assets_common': [
            ('include', 'app_name/static/src/css/web_assets_common.css'),
            ('include', 'app_name/static/src/js/web_assets_common.js'),
        ],
    },
    'demo': [
        ## Demo Data
        'demo/my_model_name_demo.xml',
    ],
    'external_dependencies': {
        'python': [
            'werkzeug',
        ],
    },
    'icon': '/app_name/static/description/icon.png',
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 0,
    'currency': 'EUR',
    'license': 'OPL-1',
    'contributors': [
        'Jeshad Khan <https://github.com/jeshadkhan>',
    ],
}
