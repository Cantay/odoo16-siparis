from odoo import models, fields, api
from odoo.exceptions import UserError

class SatinalmaSatir(models.Model):
    _name = 'satinalma.satinalma.satir'
    _description = 'Satinalma Satır Modeli'

    
    name = fields.Char(string='Ürün Açıklaması', tracking=True)
    product_id = fields.Many2one('product.product', string='Ürün', required=True)
    satinalma_id = fields.Many2one('satinalma.satinalma', string='Satinalma No', required=True)
    satinalma_tarihi = fields.Date(related='satinalma_id.satinalma_tarihi', string="Satinalma Tarihi", store=True)
    adet = fields.Float(string='Adet', default=2.0)
    fiyat = fields.Float(related='product_id.lst_price', string='Fiyat' )
    toplam_tutar = fields.Float(string='Toplam Tutar', compute='_compute_alttoplam', store=True )
    depo = fields.Many2one('satinalma.satinalma.depo', string='Depo')
    

    
    @api.depends('adet','fiyat')
    def _compute_alttoplam(self):
        for satir in self:
            satir.toplam_tutar = satir.adet * satir.fiyat
            
    @api.onchange('depo')
    def _onchange_depo(self):
        if self.depo and self.depo == "Ana Depo":
            if self.adet <= 3:
                self.adet = 2 * self.adet
