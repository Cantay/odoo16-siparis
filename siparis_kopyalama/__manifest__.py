{
    'name':'Sipariş Satır Koypalama',
    'description':'Müşteri sipariş Kopyalama',
    'author': 'Cantay Aktura',
    'version':'16.0.0.1',
    'license': 'AGPL-3',
    'depends': ['siparis_base'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/kopyala_views.xml',
    ],
    'website': '',
    'installable': True,
    'application': False,
}