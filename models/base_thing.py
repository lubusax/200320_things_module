from odoo import models, fields
from uuid import uuid4

class BaseThing(models.AbstractModel):
    _name = 'base.thing'
    
    name = fields.Char('Name')
    location = fields.Char('Location')
    
    _sql_constraints = [ (  'route_to_uniq',
                            'UNIQUE (route_to)',
                            'Route to thing/gate must be unique.'),
                         (  'route_from_uniq',
                            'UNIQUE (route_from)',
                            'Route from thing/gate must be unique.'),
                          (  'name_uniq',
                            'UNIQUE (name)',
                            'Name must be unique.')
                                ]

    def generate_route(self):
        result = str(fields.Datetime.now())+str(uuid4())
        result = result.replace(" ","").replace(":","").replace("-","")
        return result

    def generate_route_to(self):
        result = 'TO'+ self.generate_route()
        return result

    def generate_route_from(self):
        result = 'FROM'+ self.generate_route()
        return result

    route_to =fields.Char(
        string = 'route to thing/gate',
        help = 'route for outgoing data from the database to the thing/gate',
        default = generate_route_to,
        store = True,
        compute_sudo = False,
        readonly = True
        )
        
    route_from =fields.Char(
        string = 'route from gate',
        help = 'route for incoming data from the thing/gate to the database',
        default = generate_route_from,
        store = True,
        compute_sudo = False,
        readonly = True
        )

    can_receive = fields.Boolean(
        'can process/needs data from the database', default = True)

    can_send = fields.Boolean(
        'can send data to the database', default = True)