# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Test_newmodel(models.Model):
    _name = 'test_newmodel'
    _description = 'Test_newmodel'

    name = fields.Char('Name')
