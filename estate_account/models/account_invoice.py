from odoo import fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.move'

    property_id = fields.Many2one('estate.property', string='Property', readonly=True, copy=False)