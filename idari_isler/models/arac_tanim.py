from odoo import models, fields

class AracTanim(models.Model):
    _name = 'arac.tanim'
    _description = 'Araç Tanımları'

    arac_adi = fields.Char(string='Araç Adı', required=True) 
    plaka = fields.Char(string='Araç Plakası', required=True)
    sube = fields.Selection([
        ('1Kisim', '1. Kısım'),
        ('2Kisim', '2 Kısım'),
        ('kuzuluk', 'Kuzuluk')
    ], string='Şube', required=True, default='1Kisim')
    durum = fields.Char(string='Hareket Durumu', default='Geldi')    
    marka = fields.Char(string='Marka')    
    aktif_pasif = fields.Boolean(string='Kullanım Durumu', default=True)
    km = fields.Integer(string='Araç KM', default=0)

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, f'{record.plaka}'))
        return result
