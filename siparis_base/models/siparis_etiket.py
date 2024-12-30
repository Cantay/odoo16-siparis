from odoo import models, fields, api
from odoo.exceptions import UserError

class SiparisEtiket(models.Model):
    _name = 'siparis.siparis.etiket'
    _description = 'Sipariş Etiket'
    _inherit = ['mail.thread']
    
    name = fields.Char(string='Etiket', tracking=True)
    renk = fields.Integer(string='Renk')