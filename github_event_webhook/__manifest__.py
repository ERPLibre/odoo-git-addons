# © 2019 - Today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Github Event Webhook',
    'version': '1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'website': 'https://bit.ly/numigi-com',
    'license': 'LGPL-3',
    'category': 'Connector',
    'summary': 'Add a controller for importing events from github',
    'depends': [
        'github_event',
        'queue_job',
    ],
    'installable': True,
}
