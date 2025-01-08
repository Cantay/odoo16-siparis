from odoo import models, fields, api
from odoo.exceptions import UserError

class Satinalma(models.Model):
    _name = 'satinalma.satinalma'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Satinalma Modeli'

    name = fields.Char(string='Satinalma Kodu', required='True', default='Yeni')
    satinalma_turu = fields.Selection([
                        ('ihracat', 'İhracat'),
                        ('icpiyasa', 'İç Piyasa'),
                        ('ithalat', 'İthalat')
                    ],
                    default='ihracat', string='Satinalma Türü')
    musteri_id = fields.Many2one('res.partner', string='Müşteri Adı', required=True, tracking=True)
    satinalma_tarihi = fields.Date(string='Satinalma Tarihi', required='True', default=fields.Date.context_today)
    satinalma_satir_ids = fields.One2many('satinalma.satinalma.satir','satinalma_id', string='Satinalma' )
    image_1200 = fields.Image(string="Resim", max_width=1024, max_height=1024)
    satinalma_durum_id = fields.Many2one('satinalma.satinalma.durum', string='Durum', tracking=True)
    satinalma_etiket_ids = fields.Many2many('satinalma.satinalma.etiket','satinalma_satinalma_etiket_rel','satinalma_id','etiket_id', string='Etiket')
    satinalma_dokuman_ids = fields.Many2many('ir.attachment','satinalma_satinalma_dokuman_rel','satinalma_id','dokuman_id')
    taslak_satinalma = fields.Char(string="Taslak Satinalma Sayısı", compute="_compute_taslak_satinalma")
    
    @api.depends('satinalma_durum_id')
    def _compute_taslak_satinalma(self):
        for record in self:
            record.taslak_satinalma = self.search_count([('satinalma_durum_id.name', '=', 'Taslak')])
    
    # Onchange dedektörü ile çalışma. Field alanlarındaki güncellemeye bakar ve tetiklenir. 
    """
    @api.onchange('satinalma_durum_id')
    def _onchange_taslak_satinalma(self):
       taslak_satinalma_sayisi = self.env['satinalma.satinalma'].search_count([('satinalma_durum_id.name', '=', 'Taslak')])
       self.write({'taslak_satinalma': taslak_satinalma_sayisi})
    """
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'Yeni') == 'Yeni': 
            satinalma_turu = vals['satinalma_turu']
            sequence_code = f'{satinalma_turu}_sequence'
            vals['name'] = self.env['ir.sequence'].next_by_code(sequence_code) or 'New'
        
        if not vals.get('satinalma_durum_id'):
            vals['satinalma_durum_id'] = 2
            
        return super().create(vals)

    def open_form_view(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Form Ac',
            'view_mode': 'form',
            'res_model': 'satinalma.satinalma',
            'res_id': self.id,
            'target': 'current', # "new" tanımı ilgili formu poppup olarak açar
        }
        
    def action_satinalma_list(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Form Ac',
            'view_mode': 'tree',
            'res_model': 'satinalma.satinalma.satir',
            'res_id': self.id,
            'target': 'new', # "new" tanımı ilgili formu poppup olarak açar
            'domain': [('satinalma_id', '=', self.id)],
        }
        
    def action_onayla(self):
        for rec in self:
            # Müşteri Kontrol
            if not rec.musteri_id:
                raise UserError('Müşteri bilgisi tanımlı değil!')
            
            if not rec.satinalma_turu:
                raise UserError('Satinalma türü tanımlı değil!')
            
            rec.write({
                'satinalma_durum_id': 3
            })
            
            rec.message_post(
                body= f"Satinalma onaylandi. Satinalma No: {rec.name}",
                message_type='notification',
                subtype_xmlid='mail.mt_note'
            )
            
    def action_iptal(self):
        for rec in self:
            rec.write({
                'satinalma_durum_id': 5
            })
        
        self.message_post(
            body= f"Satinalma İptal Edildi. Satinalma No: {self.name}"
        )
        
        raise UserError(f"Satinalma İptal Edildi. Satinalma No: {self.name}")
        
