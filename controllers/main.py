from odoo import http

class ThingsGate(http.Controller):

    @http.route('/things/gates/register', auth='public')
    def RegisterNewGate(self):
        GatesModel = http.request.env['things.gate']
        if GatesModel.sudo().search(
            [('name', '=', 'Awaiting to be Confirmed')]):
            return('<h1>No New Gate created!</h1>')
        else:
            GatesModel.create({
                    'registrationConfirmed' : False,
                    'name' : 'Awaiting to be Confirmed',
                    'location' : 'Awaiting to be Confirmed',            
            })
        return('<h1>New Gate registered!</h1>')