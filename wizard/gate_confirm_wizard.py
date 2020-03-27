from odoo import models, fields
from odoo.exceptions import UserError

class GateConfirmWizard(models.TransientModel):
    _name = 'gate.confirm.wizard'
    _description = 'description'
    
    name = fields.Char(string='Gate Name')
    location = fields.Char(string='Gate Location')

    def confirm_new_gate(self):
        self.ensure_one()
        gate = self.env['things.gate'].sudo().search(
            [('name', '=', 'Awaiting to be Confirmed')])
        if gate:
            gate.write({
                'registrationConfirmed' : True,
                'name' : self.name,
                'location' : self.location,
                })
        else:
            raise UserError('There is no Gate '
                            'awaiting to be confirmed')
            