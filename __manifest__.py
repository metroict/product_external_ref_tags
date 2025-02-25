# -*- coding: utf-8 -*-
{
    'name': 'Product External References by Customer',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'price': 150.8,
    'currency': 'USD',
    'summary': 'Store customer-specific external references for products and seamlessly integrate them in sales and purchase orders.',
    'description': """
Product External References by Customer
=========================================

Overview:
---------
This module allows you to maintain multiple external references for products on a per-customer basis. It extends the product, supplier info, purchase order, and sales order models to provide:

* A dedicated tab on product templates to manage external references.
* Datasheet URL support in supplier information and purchase order lines.
* Enhanced sales order functionality with multiple reference types (Internal, External, and Vendor).
* A recompute feature to update order line descriptions based on the selected reference type.

Key Features:
-------------
- **Customer-Specific External References:** Maintain unique product codes per customer.
- **Datasheet URL Management:** Easily access vendor datasheets directly from supplier and order views.
- **Enhanced Sales Workflow:** Automatically update sales order line descriptions and attach vendor datasheet URLs.
- **Seamless Integration:** Inherits and extends core views of products, purchase orders, and sales orders.
- **Easy Configuration:** Setup is straightforward and fully documented.

Installation:
-------------
1. Place the module folder in your Odoo custom addons directory.
2. Update the App List and install the module.
3. Configure your products, suppliers, and customers as needed.

Support & Updates:
------------------
For support, please contact our support team at support@odoo.co.ke.
We are committed to providing updates for compatibility with future Odoo versions and addressing any bugs promptly.

Price: USD 199

License: LGPL-3
    """,
    'author': 'Metro Ict Limited',
    'license': 'LGPL-3',
    'depends': ['sale_management', 'product', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_external_ref_views.xml',
        'views/product_supplierinfo_form_view.xml',
        'views/purchase_order_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
}
