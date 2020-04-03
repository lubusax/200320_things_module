from odoo import http

class ThingsGate(http.Controller):

    @http.route('/things/gates/create',
            type = 'json',
            auth ='public', csrf=False)
    def RegisterNewGate(self, **kwargs,):
        # create a new record things.gate
        # only if there is no things.gate
        # awaiting to be cpnfirmed

        name     = kwargs.get('name')
        location   = kwargs.get('location')

        if not name: name ="not specified"
        if not location: location ="not specified"

        print('name: ', name)
        print('location: ', location)
        
        GatesModel = http.request.env['things.gate']

        print("GatesModel Search", GatesModel.sudo().search(
            [('confirmed', '=', False)]) )
        
        if GatesModel.sudo().search(
            [('confirmed', '=', False)]):
            return {}
        else:
            newGate = GatesModel.sudo().create({
                    'confirmed' : False,
                    'name' : name,
                    'location' : location,            
            })
            newGateDict = newGate.sudo().read()[0]
            print ('newGate', newGateDict)
        return newGateDict