Appointment Geolocation
=======================

.. image:: static/description/banner.png
   :alt: Appointment Geolocation Banner
   :align: center

.. image:: static/description/icon.png
   :alt: Appointment Geolocation Icon
   :align: center

Overview
--------

Appointment Geolocation enhances the calendar event form by capturing the current geolocation (latitude and longitude) when an employee confirms check-in. It generates a clickable Google Maps link from the captured coordinates, allowing you to quickly view the appointment location on a map.

Features
--------

- **Geolocation Capture:** Automatically records latitude and longitude upon check-in.
- **Clickable Map Link:** Creates a Google Maps URL from the recorded coordinates.
- **Integrated Check-In:** Adds a **Confirm Check-In** button to the appointment form.
- **Gantt View Integration:** Provides a **Capture Location** button in the Gantt popover.
- **Reset Functionality:** Offers a way to reset the geolocation fields to 0.0.

Installation
------------

1. **Place Module:**  
   Copy the module folder into your custom addons directory.

2. **Update Odoo:**  
   Restart your Odoo server and update the Apps list.

3. **Install Module:**  
   Find **Appointment Geolocation** in the Apps menu and install it.

Usage
-----

- **Calendar Event Form:**  
  Open an appointment to view additional geolocation fields (latitude, longitude, and a clickable map link). Click the **Confirm Check-In** button to capture your geolocation.

- **Gantt View:**  
  Use the **Capture Location** button in the Gantt popover to quickly record your geolocation.

Screenshots
-----------

- **Gantt View Popover:**  

  .. image:: static/description/screenshot_gantt_view_popover.png
     :alt: Gantt View Popover

- **Map Link Preview:**  

  .. image:: static/description/screenshot_map_link.png
     :alt: Map Link Preview

FAQ
---

**Q: What happens if my browser doesn't support geolocation?**  
A: The module displays a notification and falls back to the default check-in behavior.

**Q: Can I reset the captured geolocation?**  
A: Yes, using the uncheck-in functionality resets the geolocation fields to 0.0.

**Q: How is the Google Maps link generated?**  
A: It combines the captured latitude and longitude to form a URL in the format:  
``https://www.google.com/maps?q=latitude,longitude``

Support
-------

For support or further inquiries, please contact: `support@metroict.com <mailto:support@metroict.com>`_

License
-------

This module is licensed under the LGPL-3 License.
