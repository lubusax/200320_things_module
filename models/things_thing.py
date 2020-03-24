from odoo import models, fields

class ThingsThing(models.Model):
    _name = 'things.thing'
    _inherit = ['base.thing']

    # every thing sends and/or receives data
    # through one and only one gate
    gate_id = fields.Many2one('things.gate',
                string='Gate',
                required = True)

class ThingsGate(models.Model):
    _inherit = 'things.gate'

    thing_ids = fields.One2many('things.thing',
        'gate_id', string='Things attached')