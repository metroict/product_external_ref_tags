from odoo import models, fields, api

class CalendarEventInherit(models.Model):
    _inherit = "calendar.event"

    latitude = fields.Float(string="Latitude", help="Captured geolocation latitude")
    longitude = fields.Float(string="Longitude", help="Captured geolocation longitude")

    # Computed field that returns a clickable Google Maps link
    location_url = fields.Char(
        string="Map Link",
        compute="_compute_location_url",
        store=False
    )

    @api.depends('latitude', 'longitude')
    def _compute_location_url(self):
        for rec in self:
            if rec.latitude and rec.longitude:
                # Example: https://www.google.com/maps?q=-1.286389,36.817223
                rec.location_url = f"https://www.google.com/maps?q={rec.latitude},{rec.longitude}"
            else:
                rec.location_url = False



    def action_confirm_checkin(self):
        """
        Triggered when the 'Confirm Check-In' button is clicked.
        """
        self.ensure_one()
        return {
            'type': 'ir.actions.client',
            'tag': 'appointment_geolocation.confirm_checkin',  # ? Matches JS action
            'params': {'event_id': self.id},
        }
