# Frequently Asked Questions

## Q: What happens if my browser doesn't support geolocation?
A: The module will display a notification and fall back to the standard check-in process without capturing geolocation.

## Q: Can I reset the captured geolocation?
A: Yes, the module provides an "Uncheck-In" functionality that resets the latitude and longitude fields to 0.0.

## Q: How is the Google Maps link generated?
A: The module uses the captured latitude and longitude to create a URL in the format:  
`https://www.google.com/maps?q=latitude,longitude`

## Q: What are the module prerequisites?
A: Ensure that the following modules are installed before installing Appointment Geolocation:  
- appointment  
- calendar  
- web  
- web_gantt

## Q: How do I install the module?
A: Simply copy the module into your custom addons directory, restart your Odoo server, update the app list, and install the module from the Apps menu.
