from odoo import api, fields, models, _


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    log_refueling = fields.One2many('fleet.vehicle.log.refueling', 'vehicle_id', 'Refueling Logs')
    refueling_count = fields.Integer(compute="_compute_refueling_count", string='Refueling Count')

    def _compute_refueling_count(self):
        for record in self:
            record.refueling_count = self.env['fleet.vehicle.log.refueling'].search_count([('vehicle_id', '=', record.id)])

    def open_refueling_logs(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Refueling Logs'),
            "views": [[False, "tree"], [False, "form"]],
            'res_model': 'fleet.vehicle.log.refueling',
            'domain': [('vehicle_id', '=', self.id)],
            'context': {'default_vehicle_id': self.id}
        }