{
    "name": "Appointment Geolocation",
    "version": "17.0.1.0.0",
    "summary": "Capture and store geolocation on appointment checkin",
    "description": "This module captures the current geolocation when an employee confirms checkin on an appointment.",
    "category": "Tools",
    "author": "Metro Ict Limited",
    "website": "https://odoo.co.ke",
    "license": "LGPL-3",
    "depends": [
        "appointment",
        "calendar",
        "web",
        "web_gantt"

    ],
    "data": [
        "views/calendar_event_form_inherit.xml",
        "views/actions.xml",
        "views/calendar_event_tree_inherit.xml",
    ],


    "assets": {
        "web.assets_backend": [
            "appointment_geolocation/static/src/js/geolocation_action.js",
            "appointment_geolocation/static/src/js/geolocation_gantt_popover.js",
            "appointment_geolocation/static/src/js/override_gantt_checkin.js",
            "appointment_geolocation/static/src/xml/geolocation_gantt_popover.xml",

        ]
    },


    "installable": True,
    "application": False,
    "auto_install": False,
    'icon': '/appointment_geolocation/static/description/icon.png',  # Path to the icon file
    'images': ['static/description/banner.png'],
}
