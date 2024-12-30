from odoo import models, fields, api
from odoo.exceptions import UserError

class SiparisSatir(models.Model):
    _name = 'siparis.siparis.satir'
    _description = 'Sipariş Satır Modeli'

    
    name = fields.Char(string='Ürün Açıklaması', tracking=True)
    product_id = fields.Many2one('product.product', string='Ürün', required=True)
    siparis_id = fields.Many2one('siparis.siparis', string='Siparis No', required=True)
    siparis_tarihi = fields.Date(related='siparis_id.siparis_tarihi', string="Siparis Tarihi", store=True)
    adet = fields.Float(string='Adet', default=1.0)
    fiyat = fields.Float(related='product_id.lst_price', string='Fiyat' )
    toplam_tutar = fields.Float(string='Toplam Tutar', compute='_compute_alttoplam', store=True )
    depo = fields.Many2one('siparis.siparis.depo', string='Depo')
    
    @api.depends('adet','fiyat')
    def _compute_alttoplam(self):
        for satir in self:
            satir.toplam_tutar = satir.adet * satir.fiyat
            
    @api.onchange('depo')
    def _onchange_depo(self):
        if self.depo and self.depo == "Ana Depo":
            if self.adet <= 3:
                self.adet = 2 * self.adet
