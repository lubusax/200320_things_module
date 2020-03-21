from odoo import models, fields
from uuid import uuid4

class ThingsGate(models.Model):
    _name = 'things.gate'
    
    name = fields.Char('Gate Name')
    location = fields.Char('Gate Location')
    route_to_gate =fields.Char(
        string = 'route to gate',
        help = 'route for outgoing data from the database to the gate',
        default = lambda self: (
            str(fields.Datetime.now())+str(uuid4())).
            replace(" ","").
            replace(":","").
            replace("-","") ,
        store = True,
        compute_sudo = False,
        readonly = True
        )
    route_from_gate =fields.Char(
        'route for incoming data from the gate to the database')
    
    # def _compute_route_to_gate(self):
    #     self.ensure_one()
    #     self.route_to_gate = str(self.id.hex)+str(uuid.uuid4().hex) 

