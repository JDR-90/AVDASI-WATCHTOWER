from TELEMETRY_CSV_ROUTER import start_csv_logging, on_plot_close
from FC_CONNECT_ROUTER import (
    connection_start, run_status_refresh, stop_router,
    get_latest_attitude, get_latest_servos, find_servo_pos, get_latest_sensor
)
from Reading_flap_angle import *
import threading
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
import time
import numpy as np

mavlink_connection = None

def _event_close(event=None):
    # Stop CSV first (flushes), then stop router
    try:
        on_plot_close(event)
    finally:
        pass

def _update(frame):

    global _last_att_t, _last_srv_t, _last_sns_t,_counter,mavlink_connection

    now = time.time()
    t = now - start_time

    att = get_latest_attitude()
    if att is not None:
        t_att, roll, pitch, yaw = att  # FC_CONNECT_ROUTER returns (t, roll, pitch, yaw)
        if _last_att_t is None or t_att > _last_att_t:
            _last_att_t = t_att

            time_attitude.append(t)
            pitch_data.append(np.degrees(pitch))
            roll_data.append(np.degrees(roll))
            yaw_data.append(np.degrees(yaw))

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

    sns= get_latest_sensor()
    if sns is not None:
        t_sns,name,value = sns
        if _last_sns_t is None or t_sns > _last_sns_t:
            _last_sns_t = t_sns
            sensor_time_data.append(t)
            sensor_data.append(value)
    
    # Update artists
    if len(time_attitude)>0:
         pitch_line.set_data(time_attitude, pitch_data)
         roll_line.set_data(time_attitude, roll_data)
         yaw_line.set_data(time_attitude, yaw_data)
    
    if len(time_servo)>0:
        t_s=(time_servo)
        p_flap_line.set_data(t_s, p_flap_data)
        s_flap_line.set_data(t_s, s_flap_data)
        p_aileron_line.set_data(t_s,p_aileron_data)
        s_aileron_line.set_data(t_s, s_aileron_data)
        p_elevator_line.set_data(t_s,p_elevator_data)
        s_elevator_line.set_data(t_s,s_elevator_data)
        rudder_line.set_data(t_s, rudder_data)

    if len(sensor_time_data)>0 and len(sensor_time_data)==len(sensor_data):
        sensor_line.set_data(list(sensor_time_data), list(sensor_data))

    if _counter % rescale_every == 0:
        for ax in axs:
            ax.relim()
            ax.autoscale_view()

    _counter += 1
    return (pitch_line, roll_line, yaw_line,
            p_flap_line, s_flap_line, p_elevator_line, s_elevator_line, rudder_line, sensor_line)


# Interval in ms. 20ms = 50 Hz UI updates (usually plenty and keeps the window responsive).

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

    _last_att_t = None
    _last_srv_t = None
    _last_sns_t = None




    # -----------------------------
    # Figure setup
    # -----------------------------

    plt.style.use("fast")
    fig, axs = plt.subplots(3, 1, sharex=True)


    fig.canvas.mpl_connect("close_event", _event_close)

    print("\nLive plotting started...")

    # attitude plot
    pitch_line, = axs[0].plot([], [], label="Pitch")
    roll_line,  = axs[0].plot([], [], label="Roll")
    yaw_line,   = axs[0].plot([], [], label="Yaw")
    axs[0].set_ylabel("Degrees")
    axs[0].legend()
    axs[0].grid(True)

    # surface plot
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


    #sensor plot
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
    csv_path = start_csv_logging(prefix="telemetry", flush_every=20, poll_hz=200)


    # -----------------------------
    # Initial servo positions
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
