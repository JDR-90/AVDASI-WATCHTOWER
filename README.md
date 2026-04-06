
# AVDASI-WATCHTOWER
University of Bristol Aerospace Engineering: Software intended to retrieve telemetry data and control an ArduPilot/MAVLink drone system. Both Wings and Fuselage each have a separate FC onboard and so is a quasi-unified system

![Company Logo](https://github.com/user-attachments/assets/e5c6b8b8-5865-4346-a377-82eda833eedc)
<img width="300" height="300" alt="watchtower" src="https://github.com/user-attachments/assets/fda6af65-95b0-40c1-b9d4-f11155163caa" />
<img width="800" height="250" alt="UOBLOGO (1)" src="https://github.com/user-attachments/assets/4b11e2eb-85fe-4673-80ad-3330b5a18605" />



## Version 05.2026.005

- The final version of WATCHTOWER

- ANGLE_COMMAND — Removed the kit-specific initial override packet logic from the connection handler, replacing it with a zeroed default that gets set correctly by FC_CONNECT_ROUTER on connection. Added detailed comments throughout explaining the purpose of each function.

- ANGLE_CONVERSION — Minor recalibration of the starboard aileron linear conversion constants. Comments added throughout.

- FC_CONNECT_ROUTER — Now imports the override channel list directly from ANGLE_COMMAND and sets the kit-specific neutral values into it at connection time, centralising neutral value assignment. Comments added throughout.

- MAIN — Comments and section headers added throughout.

- PLOTTING — Removed the unused mavlink imports, added detailed comments throughout explaining each section's purpose.

- TELEMETRY_CSV_ROUTER — CSV files now save to a dedicated telemetry folder inside the user's Documents directory rather than the script directory, creating the folder if it doesn't exist. Removed the import of Reading_flap_angle. Comments added throughout.

- hook-pymavlink — Now also collects pymavlink data files in addition to submodules, ensuring all assets are bundled when compiling to an executable.

- MODE_SWITCH — Comments added, otherwise unchanged.

## Version 04.2026.004

- Merged separate folders into a unified script

- ANGLE_CONVERSION — Added linear conversions for port flap and a port flap sensor, and populated the port aileron lookup dictionary with real calibrated values replacing the previous zeros.

- ANGLE_COMMAND — The initial override packet now uses kit-specific neutral values selected based on the connected kit number, replacing the single hardcoded set of values. Port flap now also uses the linear conversion instead of the lookup table.

- FC_CONNECT_ROUTER — The heartbeat wait is restored (previously commented out), with a 5-second timeout added to both the connection and heartbeat calls. Target system and component are now properly set from the heartbeat source again.

- TELEMETRY_CSV_ROUTER — Kit 8 sensor conversion is now wired up to the port flap sensor linear conversion instead of being a placeholder. CSV column headers were also updated to include descriptive names for each servo channel.

- MAIN — The application was renamed to "W.A.T.C.H.T.O.W.E.R - Delta Blaze GUI", a splash screen displaying the watchtower logo was added on startup, and a window icon was set.

- hook-pymavlink — A PyInstaller hook file that ensures all pymavlink submodules are bundled correctly when compiling to an executable.

## Version 03.2026.003

- Angle to RC conversion separated into 2 separate folders: starboard/empennage & portside. Intend to unify as soon as possible.

- ANGLE_CONVERSION — Completely replaced the polynomial system with simple linear equations for elevator, rudder, starboard aileron, starboard flap, and a sensor-specific linear conversion. Also added a new sensor linear conversion for Kit 7, and updated the lookup dictionaries with revised calibration values for starboard flap, starboard aileron, and elevator. All polynomial parameters and helper functions were removed.

- ANGLE_COMMAND — Rudder and elevator now use the new linear conversions, starboard aileron and starboard flap also switch to linear, while port aileron and port flap continue using the lookup table approach.

- TELEMETRY_CSV_ROUTER — Now imports ANGLE_CONVERSION directly, and the Kit 7 sensor conversion is wired up to use the new sensor linear conversion rather than being a placeholder identity conversion.

## Version 03.2026.002

- ANGLE_CONVERSION — Added lookup dictionaries of manually measured RC values for all six control surfaces (starboard flap, starboard aileron, rudder, elevator, and placeholder dictionaries for port side), alongside getter functions that look up the correct RC value from these tables. The polynomial conversion is now bypassed by default, with a note to revert before wind tunnel testing.

- ANGLE_COMMAND — The initial override packet was updated with real calibrated neutral RC values for each channel. Rudder, elevator, starboard aileron, and starboard flap now use the lookup table approach instead of the polynomial conversion, while port aileron and port flap still use the polynomial method.

- MAIN — CSV logging is now started from the connection handler and passes the kit number through, and a window close handler was added to ensure the CSV logger shuts down cleanly when the application exits.

- TELEMETRY_CSV_ROUTER — Added a kit-specific sensor conversion system with per-kit calibration hooks (currently identity conversions, ready to be filled in), and the logging startup now accepts and stores the kit number to apply the correct conversion to sensor readings.

- PLOTTING — The sensor plot now passes the raw sensor value through the kit-specific conversion before displaying it, using the kit number from the router.

## Version 03.2026.001

- ANGLE_CONVERSION — Replaced the simple linear PWM conversion with a polynomial calibration system using experimentally fitted curves for all six control surfaces.

- ANGLE_COMMAND — All surface setters now use the new polynomial calibration to convert deflection angles to RC signals instead of the old linear approach. The flap channel was also changed from 6 to 5, and the initial override packet was updated accordingly.

- AngleConversion_Manual — A standalone command-line tool for manually calculating the RC signal for any control surface given a desired deflection angle.

- FC_CONNECT_ROUTER — Now also requests the sensor message type at 50Hz on connection, prints the current wall-clock time alongside telemetry rate stats, and accepts any sensor name through the router rather than filtering for the AS5600 specifically.

- MODE_SWITCH — The stabilised flight mode was changed from FBWB to FBWA.

- MAIN — Fixed a bug where the starboard auto-angle preset buttons were passing the wrong surface name, which would have caused a key lookup failure.

- TELEMETRY_CSV_ROUTER — CSV files now save to the script's own directory rather than the working directory, and a wall-clock timestamp column was added to each row.


## Version 02.2026.002

- Added temporary calibration scripts to curve fit the data to an nth order polynomial


## Version 02.2026.001

- ANGLE_COMMAND - Reworked so that control surfaces are actuated via rc channels instead of individual servo pwm. Allows for control surfaces to move when on the 'Stabilised Mode'

- FC_CONNECT_ROUTER - Allows for 3 kit connections (kit 7, 8, 9) via UDP Ports on the local network; global kit number variable added to allow other scripts to identify the kit connected and adjust control surface conversions as well as other functions. Sensor directly wired to I2C port on the FC and allows extraction of sensor angle to the API

- MAIN -  Expanded the UI to have separate port/starboard controls, 3 kit connection buttons, explicit override start/stop buttons, and flap angle presets for takeoff/cruise/landing

- PLOTTING — Added aileron channels and a third subplot for the flap angle Sensor

- TELEMETRY_CSV_ROUTER — Added a Sensor_Raw column to the CSV output for flap angle sensor data alongside the existing attitude and servo columns

