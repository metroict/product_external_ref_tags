/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component, xml } from "@odoo/owl";

export class AppointmentGeolocationAction extends Component {
    static template = xml`
        <div class="o_appointment_geolocation_action">
            <h3>Confirming Check-In...</h3>
            <p>Retrieving your geolocation. Please wait...</p>
        </div>
    `;

    setup() {
        this.actionService = useService("action");
        this.rpc = useService("rpc");
        this.notification = useService("notification");
        this.event_id = this.props.action.params.event_id;
        this.captureGeolocation();
    }

    captureGeolocation() {
        if (!navigator.geolocation) {
            this.notification.add("Geolocation is not supported by this browser.", { type: "danger" });
            return;
        }

        navigator.geolocation.getCurrentPosition(
            async (position) => {
                let latitude = position.coords.latitude;
                let longitude = position.coords.longitude;
                console.log("Retrieved Geolocation:", "Latitude =", latitude, "Longitude =", longitude);

                try {
                    const result = await this.rpc("/appointment_geolocation/checkin", {
                        event_id: this.event_id,
                        latitude: latitude,
                        longitude: longitude,
                    });

                    if (result.status === "success") {
                        this.notification.add("Geolocation updated successfully!", { type: "success" });

                        // Refresh the event form after successful check-in
                        this.actionService.doAction({
                            type: "ir.actions.act_window",
                            res_model: "calendar.event",
                            res_id: this.event_id,
                            views: [[false, "form"]],
                            target: "current",
                        });
                    } else {
                        this.notification.add("Error updating geolocation: " + result.message, { type: "danger" });
                    }
                } catch (error) {
                    this.notification.add("Error updating geolocation: " + error.message, { type: "danger" });
                }
            },
            (error) => {
                this.notification.add("Error retrieving geolocation: " + error.message, { type: "danger" });
            }
        );
    }
}

// ? Fix: Properly register the client action in Odoo 17
registry.category("actions").add("appointment_geolocation.confirm_checkin", AppointmentGeolocationAction);
