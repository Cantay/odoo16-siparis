from odoo import models, fields, api
from odoo.exceptions import UserError

class SatinalmaEtiket(models.Model):
    _name = 'satinalma.satinalma.etiket'
    _description = 'Satinalma Etiket'
    _inherit = ['mail.thread']
    
    name = fields.Char(string='Etiket', tracking=True)
    renk = fields.Integer(string='Renk')