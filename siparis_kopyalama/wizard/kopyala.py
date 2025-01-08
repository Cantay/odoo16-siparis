from odoo import models, fields, api
from odoo.exceptions import UserError

class SiparisKopyalaWizard(models.TransientModel):
    _name = 'siparis.kopyala.wizard'
    _description = "Siparis Kopyalama Wizard"
    
    siparis_id = fields.Many2one('siparis.siparis', string='Kaynak Sipariş')
    yeni_musteri = fields.Many2one('res.partner', string='Yeni Müşteri')
    yeni_siparis_tarihi = fields.Date(string='Yeni Sipariş Tarihi', required=True, default=fields.Date.context_today)
    yeni_siparis_turu  = fields.Selection(
        selection=lambda self: self._get_char_selection(),
        string="Selection Field"
    )
    siparis_satir_kopyala = fields.Boolean(string='Siparis Satiri Kopyala', default=True)
    dokuman_kopyala = fields.Boolean(string='Dokumanlari Kopyala', default=False)

    @api.model
    def _get_char_selection(self):
        """Dinamik seçim değerlerini kaynak modelden al."""
        records = self.env['siparis.siparis'].search([]).mapped('siparis_turu')
        unique_values = list(set(records))  # Benzersiz değerleri al
        return [(value, value) for value in unique_values if value]  # Selection formatına dönüştür

    @api.model
    def default_get(self, fields_list):
        res = super(SiparisKopyalaWizard, self).default_get(fields_list)
        active_id = self.env.context.get('active_id')
        if active_id:
            siparis = self.env['siparis.siparis'].browse(active_id)
            # Kontrol: 'siparis_turu' alanı seçim listesinde yer alıyor mu?
            valid_selection_values = [choice[0] for choice in self._get_char_selection()]
            if siparis.siparis_turu in valid_selection_values:
                res.update({
                    'siparis_id': siparis.id,
                    'yeni_musteri': siparis.musteri_id.id,
                    'yeni_siparis_turu': siparis.siparis_turu,
                })
        return res
    
    def action_kopyala(self):
        self.ensure_one()
        if not self.siparis_id:
            raise UserError('Kaynak sipariş bulunamadı.')
        
        vals = {
            'musteri_id': self.yeni_musteri.id,
            'siparis_tarihi': self.yeni_siparis_tarihi,
            'siparis_turu': self.siparis_id.siparis_turu,
        }
        
        if self.dokuman_kopyala:
            vals['siparis_dokuman_ids'] = [(6, 0, self.siparis_id.siparis_dokuman_ids.ids)]
            
        if self.siparis_satir_kopyala:
            siparis_satirlari = []
            for satir in self.siparis_id.siparis_satir_ids:
                siparis_satirlari.append((0, 0, {
                    'name': satir.name,
                    'product_id': satir.product_id.id,
                    'adet': satir.adet,
                    'fiyat': satir.fiyat,
                    'depo': satir.depo.id,
                }))
            vals['siparis_satir_ids'] = siparis_satirlari
            
        yeni_siparis = self.env['siparis.siparis'].create(vals)
        
        return{
            'name': 'Kopyalanan Siparis',
            'view_mode': 'form',
            'res_model': 'siparis.siparis',
            'res_id': yeni_siparis.id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }