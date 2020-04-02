from odoo import http

class ThingsGate(http.Controller):

    @http.route('/things/gates/create', auth ='public')
    def RegisterNewGate(self, **kwargs):
        # create a new record things.gate
        # only if there is no things.gate
        # awaiting to be cpnfirmed
        name     = kwargs.get('name')
        location   = kwargs.get('location')
        if not name: name ="not specified"
        if not location: location ="not specified"

        name = name.replace("_"," ")
        location = location.replace("_"," ")
        
        print('name: ', name)
        print('location: ', location)
        
        GatesModel = http.request.env['things.gate']
        
        if GatesModel.sudo().search(
            [('confirmed', '=', False)]):
            return('<h1>NO New Gate record created!</h1>')
        else:
            newGate = GatesModel.sudo().create({
                    'confirmed' : False,
                    'name' : name,
                    'location' : location,            
            })
            print ('newGate', newGate)
        return('<h1>New Gate RECORD created!</h1>')