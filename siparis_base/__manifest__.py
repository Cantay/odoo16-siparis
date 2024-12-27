{
    'name':'Sipariş Takip',
    'description':'Müşteri sipariş takibi',
    'author': 'Cantay Aktura',
    'version':'16.0.0.1',
    'license': 'AGPL-3',
    'depends': ['sale','base'],
    'data': [
        'security/ir.model.access.csv',
        'views/siparis_views.xml',
        'views/siparis_satir_views.xml',
    ],
    'website': '',
    'installable': True,
    'application': True,
}