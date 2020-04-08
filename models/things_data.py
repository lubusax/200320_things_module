from odoo import models, fields

class ThingsData(models.AbstractModel):
    _name = 'things.data'
    _description = 'description'
    
    name = fields.Char('Data Stream Name')