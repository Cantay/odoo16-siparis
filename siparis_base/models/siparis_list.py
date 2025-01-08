from odoo import models, fields, api
from odoo.exceptions import UserError

class Siparis(models.Model):
    _name = 'siparis.siparis'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Sipariş Modeli'

    name = fields.Char(string='Sipariş Kodu', required='True', default='Yeni')
    siparis_turu = fields.Selection([
                        ('ihracat', 'İhracat'),
                        ('icpiyasa', 'İç Piyasa'),
                        ('ithalat', 'İthalat')
                    ],
                    default='ihracat', string='Sipariş Türü')
    musteri_id = fields.Many2one('res.partner', string='Müşteri Adı', required=True, tracking=True)
    siparis_tarihi = fields.Date(string='Sipariş Tarihi', required='True', default=fields.Date.context_today)
    siparis_satir_ids = fields.One2many('siparis.siparis.satir','siparis_id', string='Sipariş' )
    image_1200 = fields.Image(string="Resim", max_width=1024, max_height=1024)
    siparis_durum_id = fields.Many2one('siparis.siparis.durum', string='Durum', tracking=True)
    siparis_etiket_ids = fields.Many2many('siparis.siparis.etiket','siparis_siparis_etiket_rel','siparis_id','etiket_id', string='Etiket')
    siparis_dokuman_ids = fields.Many2many('ir.attachment','siparis_siparis_dokuman_rel','siparis_id','dokuman_id')
    taslak_siparis = fields.Char(string="Taslak Siparis Sayısı", compute="_compute_taslak_siparis")
    
    @api.depends('siparis_durum_id')
    def _compute_taslak_siparis(self):
        for record in self:
            record.taslak_siparis = self.search_count([('siparis_durum_id.name', '=', 'Taslak')])
    
    # Onchange dedektörü ile çalışma. Field alanlarındaki güncellemeye bakar ve tetiklenir. 
    """
    @api.onchange('siparis_durum_id')
    def _onchange_taslak_siparis(self):
       taslak_siparis_sayisi = self.env['siparis.siparis'].search_count([('siparis_durum_id.name', '=', 'Taslak')])
       self.write({'taslak_siparis': taslak_siparis_sayisi})
    """
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'Yeni') == 'Yeni':
            siparis_turu = vals['siparis_turu']
            sequence_code = f'{siparis_turu}_sequence'
            vals['name'] = self.env['ir.sequence'].next_by_code(sequence_code) or 'New'
        return super().create(vals)

    def open_form_view(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Form Ac',
            'view_mode': 'form',
            'res_model': 'siparis.siparis',
            'res_id': self.id,
            'target': 'current', # "new" tanımı ilgili formu poppup olarak açar
        }
        
    def action_siparis_list(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Form Ac',
            'view_mode': 'tree',
            'res_model': 'siparis.siparis.satir',
            'res_id': self.id,
            'target': 'new', # "new" tanımı ilgili formu poppup olarak açar
            'domain': [('siparis_id', '=', self.id)],
        }