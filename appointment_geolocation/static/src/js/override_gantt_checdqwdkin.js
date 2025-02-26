/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { AppointmentBookingGanttPopover } from "@appointment/views/gantt/gantt_popover";
import { rpc } from "@web/core/network/rpc_service";

// Save the original method
const originalOnClickAttended = AppointmentBookingGanttPopover.prototype.onClickAttended;

/**
 * Patch the popover to capture geolocation when "Confirm Check-In" is clicked.
 */
patch(AppointmentBookingGanttPopover.prototype, {
    async onClickAttended(ev) {
        console.log("Patched onClickAttended triggered.");

        // If props.attendedState is false => we are about to confirm check-in
        // If props.attendedState is true => we are about to unconfirm check-in
        const isConfirm = !this.props.attendedState;

        if (isConfirm) {
            // Confirming check-in => capture geolocation
            if (!navigator.geolocation) {
                console.warn("Geolocation not supported. Fallback to original method.");
                return originalOnClickAttended.call(this, ev);
            }

            navigator.geolocation.getCurrentPosition(
                async (position) => {
                    const latitude = position.coords.latitude;
                    const longitude = position.coords.longitude;
                    console.log("Retrieved geolocation:", latitude, longitude);

                    try {
                        const result = await rpc({
                            route: "/appointment_geolocation/checkin",
                            params: {
                                event_id: this.props.context.id,  // ID from popover context
                                latitude,
                                longitude,
                            },
                        });
                        if (result.status === "success") {
                            console.log("Geolocation captured successfully!");
                            // Now proceed with the original logic
                            originalOnClickAttended.call(this, ev);
                        } else {
                            console.error("Error capturing geolocation:", result.message);
                        }
                    } catch (error) {
                        console.error("RPC error while capturing geolocation:", error);
                    }
                },
                (error) => {
                    console.error("Error retrieving geolocation:", error.message);
                }
            );
        } else {
            // Unconfirm check-in => you might reset geolocation or just call the original
            console.log("Unconfirming check-in. No geolocation capture needed, calling original method.");
            originalOnClickAttended.call(this, ev);
        }
    },
});
