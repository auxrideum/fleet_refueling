from odoo import api, fields, models, _


class FleetVehicleLogRefueling(models.Model):
    _name = 'fleet.vehicle.log.refueling'
    _description = 'Vehicle Refueling'

    vehicle_id = fields.Many2one('fleet.vehicle', 'Vehicle', required=True, help='Vehicle concerned by this log')
    amount = fields.Monetary('Cost')
    date = fields.Date(help='Date when the cost has been executed', default=fields.Date.today())
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    active = fields.Boolean(default=True)
    user_id = fields.Many2one('res.users', 'Responsible', default=lambda self: self.env.user, index=True)
    fuel_price = fields.Monetary(string="Fuel Price")
    quantity = fields.Float(string='Quantity', help='How much fuel has been loaded')

    def name_get(self):
        res = []

        for rec in self:
            res.append((rec.id, _("Refueling of {}".format(str(rec.date)))))

        return res
