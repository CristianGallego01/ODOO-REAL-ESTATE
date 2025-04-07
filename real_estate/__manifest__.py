{
    "name": "Real Estate in odoo",
    'version': '1.0.1',
    "depends": ["base", "sale", "account"
                
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_property_menus.xml",
    ],
    "application": True,
    "installable": True,
}