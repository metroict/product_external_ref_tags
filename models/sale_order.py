# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    ref_type = fields.Selection(
        [
            ('internal', 'Internal Ref'),
            ('external', 'External Ref'),
            ('vendor', 'Vendor Ref'),
        ],
        string='Ref Type',
        default='internal',
    )

    vendor_datasheet_url = fields.Char(
        string="Vendor Datasheet",
        help="URL from the vendor product info; only applies when ref_type = Vendor Ref."
    )

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_recompute_descriptions(self):
        """Recompute the line descriptions based on ref_type,
           also copy vendor datasheet if using Vendor Ref."""
        for order in self:
            for line in order.order_line:
                if not line.product_id:
                    continue

                product_tmpl = line.product_id.product_tmpl_id

                # CASE 1: Internal
                if line.ref_type == 'internal':
                    internal_ref = line.product_id.default_code or _("No Internal Ref")
                    line.name = f"{product_tmpl.name} - {internal_ref}"
                    line.vendor_datasheet_url = False

                # CASE 2: External
                elif line.ref_type == 'external':
                    external_refs = product_tmpl.external_ref_ids.filtered(
                        lambda ref: ref.partner_id == order.partner_id
                    )
                    if not external_refs:
                        raise UserError(_(
                            "No external reference found for product '%s' "
                            "for customer '%s'."
                        ) % (product_tmpl.name, order.partner_id.display_name))
                    ext_code = external_refs[0].code
                    line.name = f"[{ext_code}] {product_tmpl.name}"
                    line.vendor_datasheet_url = False

                # CASE 3: Vendor
                else:
                    vendor_lines = product_tmpl.seller_ids.sorted('sequence')
                    if not vendor_lines:
                        raise UserError(_(
                            "No vendor lines found for product '%s'."
                        ) % product_tmpl.name)
                    vendor_line = vendor_lines[0]
                    if not vendor_line.product_code:
                        raise UserError(_(
                            "No vendor product code defined on the main vendor line "
                            "for product '%s'."
                        ) % product_tmpl.name)
                    line.name = f"[{vendor_line.product_code}] {product_tmpl.name}"
                    line.vendor_datasheet_url = vendor_line.datasheet_url or False
