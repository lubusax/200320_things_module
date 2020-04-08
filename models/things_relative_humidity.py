from odoo import models, fields

class ThingsRelativeHumidity(models.AbstractModel):
    _name = 'things.data.rh'
    _description = 'description'
    
    relative_humidity = fields.Float('Relative Humidity[%]')