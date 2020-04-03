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

    @http.route('/things/gates/incoming/<routeFrom>',
            type = 'json',
            auth ='public', csrf=False)    
    def messageFromGate(self, routeFrom, **kwargs):
        GatesModel = http.request.env['things.gate']
        gateSending = GatesModel.sudo().search(
            [('route_from', '=', routeFrom)])
        if gateSending:
            gateSendingDict = gateSending.sudo().read()[0]
            print('gateSendingDict is ', gateSendingDict)
        
        print (' This is Original - something came from', routeFrom)
        return gateSending