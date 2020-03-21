from odoo import models, fields
from uuid import uuid4


class ThingsThing(models.Model):
    _name = 'things.thing'

    # every thing sends and/or receives data
    # through one and only one gate
    gate_id = fields.Many2one('things.gate', string='Gate')
    route_to_thing =fields.Char(
        'route for outgoing data from the database to the thing',
        default = lambda self: str(uuid4()),
        store = True,
        compute_sudo = False
        )
    route_from_thing =fields.Char(
        'route for incoming data from the thing to the database')
    can_receive = fields.Boolean(
        'can process/needs data from the database')
    can_send = fields.Boolean(
        'can send data to the database')

    # def _compute_route_to_thing(self):
    #     self.ensure_one()
    #     self.route_to_thing = str(self.id.hex)+str(uuid.uuid4().hex)

    


class ThingsGate(models.Model):
    _inherit = 'things.gate'
    thing_ids = fields.One2many('things.thing',
        'gate_id', string='Things attached')