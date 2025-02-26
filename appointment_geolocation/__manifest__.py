# -*- coding: utf-8 -*-
{
    'name': 'Appointment Geolocation',
    'version': '17.0.1.0.0',
    'category': 'Tools',
    'summary': 'Capture and store geolocation on appointment checkin',
    'description': """
Appointment Geolocation
=======================

Overview:
---------
This module enhances the calendar event form by capturing the current geolocation (latitude and longitude)
when an employee confirms check-in. A clickable Google Maps link is generated from the recorded coordinates,
providing an easy way to visualize the appointment location.

Key Features:
-------------
- **Geolocation Capture:** Automatically records latitude and longitude upon check-in.
- **Clickable Map Link:** Generates a Google Maps URL based on the captured coordinates.
- **Integrated Check-In:** Adds a "Confirm Check-In" button to the calendar event form.
- **Gantt View Integration:** Provides a "Capture Location" button in the Gantt popover for quick geolocation capture.
- **Reset Functionality:** Allows resetting the geolocation fields to 0.0 if needed.

Installation:
-------------
1. Place the module folder in your custom addons directory.
2. Restart your Odoo server and update the Apps list.
3. Install the module from the Apps menu.

Support & Updates:
------------------
For support, please contact our team at support@metroict.com.
We are committed to providing timely updates for compatibility with future Odoo versions.

License: LGPL-3
    """,
    'author': 'Metro Ict Limited',
    'website': 'https://odoo.co.ke',
    'license': 'LGPL-3',
    'depends': ['appointment', 'calendar', 'web', 'web_gantt'],
    'data': [
        'views/calendar_event_form_inherit.xml',
        'views/actions.xml',
        'views/calendar_event_tree_inherit.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'appointment_geolocation/static/src/js/geolocation_action.js',
            'appointment_geolocation/static/src/js/geolocation_gantt_popover.js',
            'appointment_geolocation/static/src/js/override_gantt_checkin.js',
            'appointment_geolocation/static/src/xml/geolocation_gantt_popover.xml',
        ]
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'icon': '/appointment_geolocation/static/description/icon.png',
    'images': ['static/description/banner.png'],
}
