from odoo import models, fields, api
from odoo.exceptions import UserError

class SiparisDurum(models.Model):
    _name = 'siparis.siparis.durum'
    _description = 'Sipariş Durum'
    _inherit = ['mail.thread']
    _order = 'sequence, id'

    
    name = fields.Char(string='Durum', tracking=True)
    sequence = fields.Integer(string='Sıralama', default=10)