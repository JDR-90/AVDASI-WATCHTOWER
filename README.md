
# AVDASI-WATCHTOWER
University of Bristol Aerospace Engineering: Software intended to retrieve telemetry data and control an ArduPilot/MAVLink drone system. Both Wings and Fuselage each have a separate FC onboard and so is a quasi-unified system


## Version 02.2026.001

- ANGLE_COMMAND - Reworked so that control surfaces are actuated via rc channels instead of individual servo pwm. Allows for control surfaces to move when on the 'Stabilised Mode'

- FC_CONNECT_ROUTER - Allows for 3 kit connections (kit 7, 8, 9) via UDP Ports on the local network; global kit number variable added to allow other scripts to identify the kit connected and adjust control surface conversions as well as other functions. Sensor directly wired to I2C port on the FC and allows extraction of sensor angle to the API

- MAIN -  Expanded the UI to have separate port/starboard controls, 3 kit connection buttons, explicit override start/stop buttons, and flap angle presets for takeoff/cruise/landing

- PLOTTING — Added aileron channels and a third subplot for the flap angle Sensor

- TELEMETRY_CSV_ROUTER — Added a Sensor_Raw column to the CSV output for flap angle sensor data alongside the existing attitude and servo columns

