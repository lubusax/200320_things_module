from odoo import models, fields

class GateConfirmWizard(models.TransientModel):
    _name = 'gate.confirm.wizard'
    _description = 'description'
    
    gate_id = fields.Many2one(
            'things.gate',
            string = 'Gate to be Confirmed')
    name = fields.Char(string='Gate Name')
    location = fields.Char(string='Gate Location')

    def confirm_new_gate(self):
        for wiz in self:
            wiz.gate_id.write({
                'registrationConfirmed' : True,
                'name' : wiz.name,
                'location' : wiz.location,
                })
        
            