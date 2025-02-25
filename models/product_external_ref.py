from odoo import models, fields

class ProductExternalRef(models.Model):
    """
    Stores a product's external reference code for a specific customer.
    """
    _name = 'product.external.ref'
    _description = 'Product External Reference'

    partner_id = fields.Many2one(
        'res.partner', 
        string='Customer', 
        required=True
    )
    product_template_id = fields.Many2one(
        'product.template', 
        string='Product Template', 
        required=True
    )
    code = fields.Char(
        string='External Reference', 
        required=True
    )

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    external_ref_ids = fields.One2many(
        'product.external.ref',
        'product_template_id',
        string='External References'
    )
