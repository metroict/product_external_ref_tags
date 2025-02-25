# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    datasheet_url = fields.Char(
        string="Datasheet",
        help="Link to the vendor's product datasheet from supplier info."
    )

    @api.onchange('product_id', 'order_id.partner_id')
    def _onchange_product_id_datasheet(self):
        """
        When the product or the vendor changes, look up the matching
        supplier info (seller_ids) on the product template and copy its datasheet_url.
        """
        if self.product_id and self.order_id.partner_id:
            product_tmpl = self.product_id.product_tmpl_id
            vendor_lines = product_tmpl.seller_ids.filtered(
                lambda s: s.partner_id == self.order_id.partner_id
            )
            if vendor_lines:
                self.datasheet_url = vendor_lines[0].datasheet_url
            else:
                self.datasheet_url = False
        else:
            self.datasheet_url = False
