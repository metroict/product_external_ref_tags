/** @odoo-module alias=appointment_geolocation/js/geolocation_gantt_popover **/

import { AppointmentBookingGanttPopover } from "@appointment/views/gantt/gantt_popover";
import { useService } from "@web/core/utils/hooks";
import { patch } from "@web/core/utils/patch";

// Patch the AppointmentBookingGanttPopover prototype with our new methods.
patch(AppointmentBookingGanttPopover.prototype, {
    setup() {
        // Call the original setup method.
        super.setup();
        // Initialize the RPC and notification services.
        this.rpc = useService("rpc");
        this.notification = useService("notification");
        console.log("Geolocation patch successfully applied on AppointmentBookingGanttPopover.");
    },
    onClickCaptureLocation() {
        console.log("Capture Location button clicked.");
        if (!navigator.geolocation) {
            this.notification.add("Geolocation is not supported by this browser.", { type: "danger" });
            return;
        }
        navigator.geolocation.getCurrentPosition(
            async (position) => {
                const latitude = position.coords.latitude;
                const longitude = position.coords.longitude;
                try {
                    const result = await this.rpc("/appointment_geolocation/checkin", {
                        event_id: this.props.context.id,
                        latitude: latitude,
                        longitude: longitude,
                    });
                    if (result.status === "success") {
                        this.notification.add("Geolocation captured successfully!", { type: "success" });
                        // Close the popover after successful capture.
                        this.props.close();
                    } else {
                        this.notification.add("Error capturing geolocation: " + result.message, { type: "danger" });
                    }
                } catch (error) {
                    this.notification.add("Error capturing geolocation: " + error.message, { type: "danger" });
                }
            },
            (error) => {
                this.notification.add("Error retrieving geolocation: " + error.message, { type: "danger" });
            }
        );
    },
});
