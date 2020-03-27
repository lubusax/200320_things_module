from odoo import models, fields

class ThingsGate(models.Model):
    _name = 'things.gate'
    _inherit = ['things.basis']

    registrationConfirmed = fields.Boolean(
        string='Registration Confirmed?',
        help='User confirmed the Registration of the new Gate',
        default = False)


