from odoo import models, fields, api
from odoo.exceptions import UserError

class SatinalmaDurum(models.Model):
    _name = 'satinalma.satinalma.durum'
    _description = 'Satinalma Durum'
    _inherit = ['mail.thread']
    _order = 'sequence, id'

    
    name = fields.Char(string='Durum', tracking=True)
    sequence = fields.Integer(string='Sıralama', default=10)