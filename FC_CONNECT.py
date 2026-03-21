from pymavlink import mavutil
import threading

def connection_start(kit=None):
    # For connecting to the vehicle:         Ground Station Mode -> udpin:0.0.0.0:14550 [listens to all ports, the kahuna connects to you on 14550]
    #                                        Access Point Mode -> udp:192.168.4.1:14550 [connects to the kahuna directly on its IP address]           
    if kit is None:
        kit = 8
    elif kit == '8':
        m = mavutil.mavlink_connection('udpin:0.0.0.0:14558')
    elif kit == '7':
        m = mavutil.mavlink_connection('udpin:0.0.0.0:14557')

    # Checking if connection is successful

    print('Start heartbeat search')
    msg = m.recv_match(type='HEARTBEAT', blocking=True, timeout=3)
    if msg is None:
        return None
    #m.mav.heartbeat_send(0, 0, 0, 0, 0)
    #m.wait_heartbeat()

    print('Heartbeat found')

    return m




def mavlink_status(m):
    while True:
        msg = m.recv_match(blocking=True)
        if not msg:
            continue

        if msg.get_type() == "HEARTBEAT":
            # m.flightmode updates here internally
            pass

        if msg.get_type() == "STATUSTEXT":
            print("FC:", msg.text)





def run_status_refresh(m):
    # Start status_refresh thread to run in background, daemon=True to close with main program
    listenerthread = threading.Thread(target=mavlink_status, args=(m, ), daemon=True)
    listenerthread.start()

