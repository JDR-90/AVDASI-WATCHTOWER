from pymavlink import mavutil

# -------------------------
# Connect to Cube over UDP
# -------------------------
# Replace with your Cube port if different
master = mavutil.mavlink_connection('udp:0.0.0.0:14558')

print("Listening for Pico NAMED_VALUE_FLOAT via Cube...")

while True:
    # Blocking read for NAMED_VALUE_FLOAT messages
    msg = master.recv_match(type='NAMED_VALUE_FLOAT', blocking=True)
    if msg:
        # Clean the name string (remove null bytes)
        name = msg.name.decode('utf-8').strip('\x00')
        value = msg.value
        
        # Optional: show which SYSID sent it
        sysid = msg.get_srcSystem()
        
        print(f"{name}: {value:.2f} (SYSID={sysid})")
