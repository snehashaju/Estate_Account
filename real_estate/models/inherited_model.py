from odoo import fields, models, api


class PropertyUsers(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many('estate.property','user_id',string='Property')
