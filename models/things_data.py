from odoo import models, fields

class ThingsData(models.AbstractModel):
    _name = 'things.data'
    
    name = fields.Char('Name')