from odoo import models, fields

class ThingsGate(models.Model):
    _name = 'things.gate'
    
    name = fields.Char('Gate Name')
    location = fields.Char('Gate Location')
    route_to_gate =fields.Char(
        'route for outgoing data from the database to the gate')
    route_from_gate =fields.Char(
        'route for incoming data from the gate to the database')

