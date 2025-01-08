{
    'name':'Satın Alma Takip',
    'description':'Satın Alma Takip',
    'author': 'Cantay Aktura',
    'version':'16.0.0.1',
    'license': 'AGPL-3',
    'depends': ['purchase','base'],
    'data': [
        'views/data.xml',
        'security/siparis_security.xml',
        'security/ir.model.access.csv',
        'views/siparis_siparis_views.xml',
        # 'views/siparis_satir_views.xml',
        # 'views/siparis_depo_views.xml',
        # 'views/siparis_durum_views.xml',
        # 'views/siparis_etiket_views.xml',
        # 'report/siparis_rapor.xml',
        # 'report/siparis_rapor_pdf.xml',
    ],
    # 'assets': {
    # 'web.assets_backend': [
    #     'siparis_base/static/src/css/custom.css',
    #     ],
    # },
    'website': '',
    'installable': True,
    'application': True,
}