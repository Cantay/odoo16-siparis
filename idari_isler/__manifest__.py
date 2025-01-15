{
    'name':'İdari İşler',
    'description':'İdari İşler Modülü',
    'author': 'Gazi Becit',
    'version':'16.0.0.1',
    'license': 'AGPL-3',
    'depends': ['base','hr'], # Başka bir modüle bağımlılık varsa ekleyin
    # XML dosyalarını ekleyebilirsiniz
    "data": [
        "views/arac_tanim_views.xml",
        "security/ir.model.access.csv",
        "views/arac_hareketleri_views.xml"
    ],
    # 'assets': {
    # 'web.assets_backend': [
    #     'idari_isler/static/src/css/custom.css',
    #     ],
    # },
    'website': '',
    'installable': True,
    'application': True,
}

