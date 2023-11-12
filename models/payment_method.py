```python
from odoo import models, fields, api

class PaymentMethod(models.Model):
    _name = 'payment.method'
    _description = 'Payment Method'

    name = fields.Char(string='Payment Method Name', required=True)
    payment_type = fields.Selection([
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
        ('other', 'Other'),
    ], string='Payment Type', required=True)
    associated_orders = fields.One2many('sale.order', 'payment_method_id', string='Associated Orders')
    currency_id = fields.Many2one('res.currency', string='Currency')
    active = fields.Boolean('Active', default=True)

    @api.model
    def create(self, vals):
        record = super(PaymentMethod, self).create(vals)
        # Notify about the new payment method
        self.env['bus.bus'].sendone(
            (self._cr.dbname, 'res.partner', self.env.user.partner_id.id),
            {'type': 'new_payment_method', 'record': record.read()[0]})
        return record

    @api.multi
    def write(self, vals):
        res = super(PaymentMethod, self).write(vals)
        # Notify about the updated payment method
        for record in self:
            self.env['bus.bus'].sendone(
                (self._cr.dbname, 'res.partner', self.env.user.partner_id.id),
                {'type': 'update_payment_method', 'record': record.read()[0]})
        return res
```