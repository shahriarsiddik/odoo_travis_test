from odoo import api,fields,models,_


class FleetRequisition(models.Model):
    _name = 'fleet.requisition'

    # def _get_user_name(self):
    #     u_id = self.env.employee.id
    #     return u_id
    from_time = fields.Datetime('From Time')
    to_time = fields.Datetime('To Time')
    requisition_by = fields.Many2one('res.users', 'Requisition By', readonly=True, default=lambda self: self.env.user)
    comment = fields.Text('Comment')
    approve_vehicle = fields.Many2one('fleet.vehicle', string='Approved Vehicle')
    state = fields.Selection([
        ('request', 'Request'),
        ('approval', 'Approval'),
        ('approved', 'Approved'),
        ('denied', 'Denied')

    ], string='Status', readonly=True, track_visibility='onchange', copy=False, default='request')

    def action_request(self):
        self.state = 'approval'

    def action_approved(self):
        self.state = 'approved'

    def action_denied(self):
        self.state = 'denied'

    def action_reset(self):
        self.state = 'approval'
