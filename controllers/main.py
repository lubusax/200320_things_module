from odoo import http

class ThingsGate(http.Controller):

    @http.route('/things/gates/create', auth='public')
    def RegisterNewGate(self):
        GatesModel = http.request.env['things.gate']
        if GatesModel.sudo().search(
            [('name', '=', 'Awaiting to be Confirmed')]):
            return('<h1>NO New Gate record created!</h1>')
        else:
            GatesModel.create({
                    'registrationConfirmed' : False,
                    'name' : 'Awaiting to be Confirmed',
                    'location' : 'Awaiting to be Confirmed',            
            })
        return('<h1>New Gate RECORD created!</h1>')