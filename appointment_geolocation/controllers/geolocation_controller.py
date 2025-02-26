from odoo import http
from odoo.http import request

class GeolocationController(http.Controller):

    @http.route('/appointment_geolocation/checkin', type='json', auth="user")
    def checkin(self, event_id, latitude, longitude):
        event = request.env['calendar.event'].browse(event_id)
        if event:
            event.sudo().write({'latitude': latitude, 'longitude': longitude})
            return {"status": "success"}
        return {"status": "error", "message": "Event not found"}

    @http.route('/appointment_geolocation/uncheckin', type='json', auth="user")
    def uncheckin(self, event_id):
        """
        Reset the geolocation fields to 0.0 for the given event_id
        """
        event = request.env['calendar.event'].browse(event_id)
        if event:
            event.sudo().write({'latitude': 0.0, 'longitude': 0.0})
            return {"status": "success"}
        return {"status": "error", "message": "Event not found"}