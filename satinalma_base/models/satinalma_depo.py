from odoo import models, fields, api
from odoo.exceptions import UserError

class SatinalmaDepo(models.Model):
    _name = 'satinalma.satinalma.depo'
    _description = 'Satinalma Mal Deposu'

    
    name = fields.Char(string='Depo Adı', tracking=True)