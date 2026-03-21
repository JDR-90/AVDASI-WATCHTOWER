############################################################
#####                    PLOTTING.py                   #####
############################################################

###
### Purpose: Live plotting of telemetry data received from the flight controller, including attitude, servo positions, and sensor readings
###
### Script Dependencies: TELEMETRY_CSV_ROUTER.py (for logging telemetry data to CSV), FC_CONNECT_ROUTER.py (for accessing latest telemetry data from the flight controller)
###
### Library Dependencies: matplotlib (for plotting), collections (for data buffering), time (for timing), numpy (for data manipulation)
###
### See below for more detail on functionality 







from TELEMETRY_CSV_ROUTER import start_csv_logging, on_plot_close, _convert_sensor_value
import FC_CONNECT_ROUTER as FC_CONNECT
from FC_CONNECT_ROUTER import (
    get_latest_attitude, get_latest_servos, find_servo_pos, get_latest_sensor
)
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
import time
import numpy as np




mavlink_connection = None


# Allows for the UI to close the CSV without losing data
def _event_close(event=None):
    # Stop CSV first (flushes), then stop router
    try:
        on_plot_close(event)
    finally:
        pass




############################################################
### Main update function for Plot. Called every interval ###
############################################################

def _update(frame):

    global _last_att_t, _last_srv_t, _last_sns_t, _counter, mavlink_connection


    # Relative time in seconds since start of plotting
    now = time.time()
    t = now - start_time


    # Get latest data from router and adds to the buffers if the data is new (compared to the last timestamp for that data type)
    att = get_latest_attitude()

    if att is not None:

        t_att, roll, pitch, yaw = att 

        if _last_att_t is None or t_att > _last_att_t:
            _last_att_t = t_att

            time_attitude.append(t)
            pitch_data.append(np.degrees(pitch))
            roll_data.append(np.degrees(roll))
            yaw_data.append(np.degrees(yaw))


    # Gets the latest servo positions and adds to the buffers if there's new data (compared to last servo timestamp)
    srv = get_latest_servos()
    if srv is not None:
        t_srv = srv[find_servo_pos("time")]
        if _last_srv_t is None or t_srv > _last_srv_t:
            _last_srv_t = t_srv

            time_servo.append(t)
            p_flap     = srv[find_servo_pos("p_flap")]
            s_flap     = srv[find_servo_pos("s_flap")]
            p_aileron  = srv[find_servo_pos("p_aileron")]
            s_aileron  = srv[find_servo_pos("s_aileron")]
            p_elevator = srv[find_servo_pos("p_elevator")]
            s_elevator = srv[find_servo_pos("s_elevator")]
            rudder     = srv[find_servo_pos("rudder")]

            p_flap_data.append(p_flap)
            s_flap_data.append(s_flap)
            p_aileron_data.append(p_aileron)
            s_aileron_data.append(s_aileron)
            p_elevator_data.append(p_elevator)
            s_elevator_data.append(s_elevator)
            rudder_data.append(rudder)



    # Gets the latest sensor reading and adds to the buffer if there's new data (compared to last sensor timestamp)
    sns = get_latest_sensor()
    if sns is not None:
        t_sns,name,value = sns
        if _last_sns_t is None or t_sns > _last_sns_t:
            _last_sns_t = t_sns
            sensor_time_data.append(t)
            converted_value = _convert_sensor_value(value, FC_CONNECT.kit_number)
            sensor_data.append(converted_value)
    


    # Update the plot lines with the new data. Only updates if there's at least one data point to avoid errors
    if len(time_attitude)>0:
         pitch_line.set_data(time_attitude, pitch_data)
         roll_line.set_data(time_attitude, roll_data)
         yaw_line.set_data(time_attitude, yaw_data)
    

    # Update servo lines if we have servo data to avoid errors
    if len(time_servo)>0:
        t_s=(time_servo)
        p_flap_line.set_data(t_s, p_flap_data)
        s_flap_line.set_data(t_s, s_flap_data)
        p_aileron_line.set_data(t_s,p_aileron_data)
        s_aileron_line.set_data(t_s, s_aileron_data)
        p_elevator_line.set_data(t_s,p_elevator_data)
        s_elevator_line.set_data(t_s,s_elevator_data)
        rudder_line.set_data(t_s, rudder_data)


    # Update sensor line if we have sensor data to avoid errors
    if len(sensor_time_data)>0 and len(sensor_time_data)==len(sensor_data):
        sensor_line.set_data(list(sensor_time_data), list(sensor_data))


    # Rescale the axes every few frames to keep the plot looking good as new data comes in
    if _counter % rescale_every == 0:
        for ax in axs:
            ax.relim()
            ax.autoscale_view()



    _counter += 1

    # Returns the updated plot lines
    return (pitch_line, roll_line, yaw_line,
            p_flap_line, s_flap_line, p_elevator_line, s_elevator_line, rudder_line, sensor_line)


# Interval in ms. 20ms = 50 Hz UI updates

def _run_plot(mavlink=None):
    global mavlink_connection
    mavlink_connection = mavlink
    
    global fig, axs
    global pitch_line, roll_line, yaw_line
    global p_flap_line, s_flap_line, p_elevator_line, s_elevator_line, rudder_line, sensor_line
    global s_aileron_line, p_aileron_line
    global sensor_time_data, sensor_data
    global start_time, _counter
    global time_attitude, pitch_data, roll_data, yaw_data
    global time_servo, p_flap_data, s_flap_data, p_elevator_data, s_elevator_data, rudder_data, s_aileron_data, p_aileron_data
    global _last_att_t, _last_srv_t, _last_sns_t
    global rescale_every



    # -----------------------------
    # Plot buffers / parameters
    # -----------------------------
    max_points = 600
    rescale_every = 3  # frames

    # Deque is a buffer that automatically discards old data when it exceeds the max length. 
    # Note that the csv script keeps the full history, this is for memory management in the plot only
    time_attitude   = deque(maxlen=max_points)
    time_servo      = deque(maxlen=max_points)
    sensor_time_data= deque(maxlen=max_points) 
    pitch_data      = deque(maxlen=max_points)
    roll_data       = deque(maxlen=max_points)
    yaw_data        = deque(maxlen=max_points)

    p_flap_data     = deque(maxlen=max_points)
    s_flap_data     = deque(maxlen=max_points)
    p_aileron_data  = deque(maxlen=max_points)
    s_aileron_data  = deque(maxlen=max_points)
    p_elevator_data = deque(maxlen=max_points)
    s_elevator_data = deque(maxlen=max_points)
    rudder_data     = deque(maxlen=max_points)

    sensor_data     = deque(maxlen=max_points)

    # Initialize last timestamps for each data type to None 
    # This will be used to determine if new data has arrived since the last plot update.
    _last_att_t = None
    _last_srv_t = None
    _last_sns_t = None




    # -----------------------------
    # Figure setup
    # -----------------------------

    plt.style.use("fast")
    fig, axs = plt.subplots(3, 1, sharex=True)      # 3 rows of plots, 1 column, shared x-axis


    fig.canvas.mpl_connect("close_event", _event_close)

    print("\nLive plotting started...")

    # Attitude Plot (Top Plot)
    pitch_line, = axs[0].plot([], [], label="Pitch")
    roll_line,  = axs[0].plot([], [], label="Roll")
    yaw_line,   = axs[0].plot([], [], label="Yaw")
    axs[0].set_ylabel("Degrees")
    axs[0].legend()
    axs[0].grid(True)

    # Servo Plot (Middle Plot)
    p_flap_line,     = axs[1].plot([], [], label="P_Flap")
    s_flap_line,     = axs[1].plot([], [], label="S_Flap")
    p_aileron_line,  = axs[1].plot([], [], label="P_Aileron")
    s_aileron_line,  = axs[1].plot([], [], label="S_Aileron")
    p_elevator_line, = axs[1].plot([], [], label="P_Elevator")
    s_elevator_line, = axs[1].plot([], [], label="S_Elevator")
    rudder_line,     = axs[1].plot([], [], label="Rudder")

    axs[1].set_ylabel("Servo PWM")
    axs[1].set_xlabel("Time (s)")
    axs[1].legend()
    axs[1].grid(True)


    # Sensor Plot (Bottom Plot)
    sensor_line, = axs[2].plot([], [], label="Flap Angle Sensor")
    axs[2].set_ylabel("Degrees")
    axs[2].set_xlabel("Time (s)")
    axs[2].legend()
    axs[2].grid(True)

    start_time = time.time()
    _counter = 0


    # -----------------------------
    # CSV logging
    # -----------------------------
    csv_path = start_csv_logging(prefix="telemetry", flush_every=20, poll_hz=200) # starts logging in background, flushes (saves data to csv and clears buffer) every 20 rows, polls router at 200 Hz


    # -----------------------------
    # Initial servo positions (Helpful for debugging when issues occured with control surfaces)
    # -----------------------------
    print("\nInitial servo positions:")
    servo_data = None
    while servo_data is None:
        servo_data = get_latest_servos()
        if servo_data is None:
            time.sleep(0.05)

    for i in range(1, 9):
        pwm = servo_data[i]
        print(f"Servo {i} PWM: {pwm}")



    ani = FuncAnimation(fig, _update, interval=20, blit=False, cache_frame_data=False)
    plt.show(block=False)

    return ani
