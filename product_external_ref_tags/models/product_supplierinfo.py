# -*- coding: utf-8 -*-
from odoo import fields, models

class ProductSupplierinfo(models.Model):
    _inherit = "product.supplierinfo"

    active = fields.Boolean(default=True)

    datasheet_url = fields.Char(
        string='Datasheet',
        help="Optional link to the vendor's product datasheet for this product."
    )
