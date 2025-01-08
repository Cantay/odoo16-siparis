from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class SiparisKontrol(models.Model):
    _inherit = 'siparis.siparis.satir'
    
    @api.constrains('adet')
    def _check_adet(self):
        if self.adet < 2:
            raise ValidationError("Adet sayısı 2'den küçük olamaz!")
        
    @api.onchange('adet')
    def _onchage_adet(self):
        if self.adet < 2:
            return {
                'warning': {
                    'title': 'Adet Sayısı Hatası',
                    'message': '2 Adet altı veremezsiniz.'
                }
            }