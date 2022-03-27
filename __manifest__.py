# -*- coding: utf-8 -*-
{
    'name': "Fleet Refueling",

    'summary': "Adds support for tracking refuelings in Fleet",

    'author': "Gabriele Portente",
    'website': "https//gabrieleportente.it",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['fleet'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_views.xml',
        'views/fleet_vehicle_refueling_view.xml',

    ],
}
