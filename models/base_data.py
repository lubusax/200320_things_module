from odoo import models, fields

class BaseData(models.AbstractModel):
    _name = 'base.data'
    
    name = fields.Char('Name')