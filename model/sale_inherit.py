from odoo import models, fields


class SaleInherit(models.Model):
    _inherit = 'sale.order'

    upload_image = fields.Image(string="UploadImage")
    resolutions = fields.Image(related='upload_image', max_hight=100,
                               max_width=100, string='Resolution-100x100')
    resolution = fields.Image(related='upload_image', max_hight=400,
                              max_width=400, string='Resolution-200x200')
