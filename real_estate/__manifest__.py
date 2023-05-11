# -*- coding: utf-8 -*-
{
    'name': "Real Estate",
    'author': "Sneha",
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/properties_views.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/inherited_user_views.xml',

    ],
    'images': [
        'static/description/icon.png',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
