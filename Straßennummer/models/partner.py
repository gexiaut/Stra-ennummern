# # -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    streetnumber = fields.Char(string="Straßennummer")
