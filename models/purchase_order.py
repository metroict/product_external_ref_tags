# -*- coding: utf-8 -*-
from odoo import models, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('partner_id')
    def _onchange_partner_id_recompute_lines(self):
        """
        When the vendor (partner_id) on the Purchase Order changes,
        force each order line to recalculate its datasheet field.
        """
        for line in self.order_line:
            line._onchange_product_id_datasheet()
