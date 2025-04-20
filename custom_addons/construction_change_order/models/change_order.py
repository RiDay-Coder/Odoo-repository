from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ConstructionChangeOrder(models.Model):
    _name = "construction.change_order"
    _description = "Construction Change Order"
    _order = "create_date desc"

    name = fields.Char(string="Reference", required=True, default=lambda self: self.env['ir.sequence'].next_by_code('construction.change_order'))
    project_id = fields.Many2one("project.project", string="Project", required=True)
    change_type = fields.Selection([
        ('scope', 'Scope'),
        ('time', 'Time'),
        ('cost', 'Cost'),
        ('all', 'All')
    ], string="Change Type", required=True)
    description = fields.Text(string="Description", required=True)
    reason = fields.Text(string="Reason")
    date_requested = fields.Date(string="Requested Date", default=fields.Date.today)
    requested_by = fields.Many2one("res.users", string="Requested By", default=lambda self: self.env.user)
    cost_impact = fields.Float(string="Cost Impact")
    status = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string="Status", default="draft")
    approver_id = fields.Many2one("res.users", string="Approved By")
    date_approved = fields.Date(string="Approval Date")

    def action_submit(self):
        for rec in self:
            rec.status = 'submitted'

    def action_approve(self):
        for rec in self:
            rec.status = 'approved'
            rec.approver_id = self.env.user
            rec.date_approved = fields.Date.today()

    def action_reject(self):
        for rec in self:
            rec.status = 'rejected'
            rec.approver_id = self.env.user
            rec.date_approved = fields.Date.today()
