{
    'name': 'Hospital Management',
    'version': '12.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Module for managing Hospitals',
    'sequence': '1',
    'license': 'AGPL-3',
    'author': 'Sumesh Majhi',
    'maintainer': 'MajhiRockzZ',
    'website': 'https://www.majhirockzz.me/',
    'depends': [
        'base',
        'mail',
        'sale'

    ],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/data.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'reports/report.xml',
        'reports/patient_card.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
