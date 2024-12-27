from odoo import models, fields, api
from odoo.exceptions import UserError

class SiparisDepo(models.Model):
    _name = 'siparis.siparis.depo'
    _description = 'Sipariş Mal Deposu'

    
    name = fields.Char(string='Depo Adı', tracking=True)