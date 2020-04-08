from odoo import models, fields

class ThingsTemperatureCelsius(models.AbstractModel):
    _name = 'things.data.celsius'
    _description = 'description'
    
    temperature_celsius = fields.Float('T[°C]')