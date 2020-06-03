# Copyright 2020 Lorenzo Battistini @ TAKOBI
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    "name": "Progressive web application - Portal",
    "summary": "Make Odoo portal a PWA",
    "version": "12.0.1.0.0",
    "development_status": "Beta",
    "category": "Website",
    "website": "https://github.com/OCA/website",
    "author": "TAKOBI, Odoo Community Association (OCA)",
    "maintainers": ["eLBati"],
    "license": "LGPL-3",
    "application": True,
    "installable": True,
    "depends": [
        'portal',
    ],
    "data": [
        "views/webclient_templates.xml",
    ],
    'qweb': [
        'static/src/xml/pwa_install.xml',
    ],
    'images': ['static/description/pwa.png'],
}
