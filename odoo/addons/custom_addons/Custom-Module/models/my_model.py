from odoo import models, fields

class MyModel(models.Model):
    _name = 'my.custom.model'
    _description = 'My Custom Model'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")

