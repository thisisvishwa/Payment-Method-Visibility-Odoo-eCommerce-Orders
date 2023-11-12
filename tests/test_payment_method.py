```python
from odoo.tests import common

class TestPaymentMethod(common.TransactionCase):

    def setUp(self):
        super(TestPaymentMethod, self).setUp()
        self.PaymentMethod = self.env['payment.method']

    def test_01_check_payment_method(self):
        # Create a new payment method
        self.payment_method = self.PaymentMethod.create({
            'name': 'Test Payment Method',
            'type': 'Credit Card',
        })

        # Check if payment method is created
        self.assertEqual(self.payment_method.name, 'Test Payment Method')
        self.assertEqual(self.payment_method.type, 'Credit Card')

    def test_02_check_payment_method_update(self):
        # Update the payment method
        self.payment_method.write({
            'name': 'Updated Payment Method',
        })

        # Check if payment method is updated
        self.assertEqual(self.payment_method.name, 'Updated Payment Method')

    def test_03_check_payment_method_delete(self):
        # Delete the payment method
        self.payment_method.unlink()

        # Check if payment method is deleted
        self.assertEqual(len(self.PaymentMethod.search([])), 0)
```