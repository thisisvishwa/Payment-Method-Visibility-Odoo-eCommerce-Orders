{
    'name': 'Enhanced Backend Payment Method Visibility',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Enhanced visibility of payment methods in backend',
    'sequence': 10,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'data/payment_method_data.xml',
        'views/payment_method_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'description': """
    This module enhances the visibility of payment methods used in eCommerce orders within Odoo's various standard views, aiding in order tracking and data-driven decision-making.
    """
}