/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { AppointmentBookingGanttPopover } from "@appointment/views/gantt/gantt_popover";

/**
 * Keep a reference to the original onClickAttended method so we can call it
 * after updating the record. We do two flows:
 *  - Confirm Check-In: capture geolocation, store lat/long
 *  - Unconfirm Check-In: reset lat/long to 0.0
 */
const originalOnClickAttended = AppointmentBookingGanttPopover.prototype.onClickAttended;

patch(AppointmentBookingGanttPopover.prototype, {
    async onClickAttended(ev) {
        console.log("Patched onClickAttended triggered. All props =", this.props);

        // If false => user is about to confirm check-in
        // If true  => user is about to unconfirm check-in
        const isConfirm = !this.props.attendedState;

        // The event ID from the popover context
        const eventId = this.props.context?.id;
        if (!eventId) {
            console.error("No eventId found in props.context. Falling back to original method.");
            return originalOnClickAttended.call(this, ev);
        }

        if (isConfirm) {
            // -------------------------------
            // CONFIRM CHECK-IN => CAPTURE GEO
            // -------------------------------
            if (!navigator.geolocation) {
                console.warn("Geolocation is not supported. Fallback to original method.");
                return originalOnClickAttended.call(this, ev);
            }

            // 1) Capture geolocation
            let position;
            try {
                position = await new Promise((resolve, reject) => {
                    navigator.geolocation.getCurrentPosition(resolve, reject);
                });
            } catch (err) {
                console.error("Error retrieving geolocation:", err.message);
                return originalOnClickAttended.call(this, ev);
            }

            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            console.log("Retrieved geolocation:", latitude, longitude);

            // 2) Send JSON-RPC style POST to /appointment_geolocation/checkin
            let data;
            try {
                const response = await fetch("/appointment_geolocation/checkin", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        jsonrpc: "2.0",
                        method: "call",
                        params: { event_id: eventId, latitude, longitude },
                        id: 1
                    })
                });
                data = await response.json();
            } catch (error) {
                console.error("Network error while capturing geolocation:", error);
                return originalOnClickAttended.call(this, ev);
            }

            // 3) Check the server response
            console.log("Response from /appointment_geolocation/checkin:", data);
            if (data.result && data.result.status === "success") {
                console.log("Geolocation captured successfully!");
                // Proceed with native check-in
                originalOnClickAttended.call(this, ev);
            } else {
                console.error("Error capturing geolocation:", data.error || data.result);
                // Optionally skip or proceed anyway
                originalOnClickAttended.call(this, ev);
            }

        } else {
            // -------------------------------
            // UNCONFIRM => RESET GEO TO 0.0
            // -------------------------------
            console.log("Unconfirming check-in => resetting lat/long to 0.0");
            let data;
            try {
                const response = await fetch("/appointment_geolocation/uncheckin", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        jsonrpc: "2.0",
                        method: "call",
                        params: { event_id: eventId },
                        id: 1
                    })
                });
                data = await response.json();
            } catch (error) {
                console.error("Network error while resetting geolocation:", error);
                return originalOnClickAttended.call(this, ev);
            }

            console.log("Response from /appointment_geolocation/uncheckin:", data);
            if (data.result && data.result.status === "success") {
                console.log("Geolocation reset to 0.0 successfully!");
                // Proceed with native unconfirm
                originalOnClickAttended.call(this, ev);
            } else {
                console.error("Error resetting geolocation:", data.error || data.result);
                // Possibly still proceed with unconfirm
                originalOnClickAttended.call(this, ev);
            }
        }
    },
});
