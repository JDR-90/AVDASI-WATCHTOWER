

# Temporary angle to PWM conversion 
def angle_to_pwm(angle, min_pwm=1000, max_pwm=2000, min_angle=int, max_angle=int):
    """
    Convert an angle in degrees to a PWM signal.

    Parameters:
    angle (float): The angle in degrees to convert.
    min_pwm (int): The minimum PWM value corresponding to min_angle.
    max_pwm (int): The maximum PWM value corresponding to max_angle.
    min_angle (float): The minimum angle in degrees.
    max_angle (float): The maximum angle in degrees.

    Returns:
    int: The corresponding PWM value.
    """
    # Clamp the angle to the specified range
    if angle < min_angle:
        angle = min_angle
    elif angle > max_angle:
        angle = max_angle

    # Linear interpolation to find the PWM value
    pwm = min_pwm + (angle - min_angle) * (max_pwm - min_pwm) / (max_angle - min_angle)
    return int(pwm)


def pwm_to_angle(pwm, min_pwm=1000, max_pwm=2000, min_angle=int, max_angle=int):
    """
    Convert a PWM signal to an angle in degrees.

    Parameters:
    pwm (int): The PWM value to convert.
    min_pwm (int): The minimum PWM value corresponding to min_angle.
    max_pwm (int): The maximum PWM value corresponding to max_angle.
    min_angle (float): The minimum angle in degrees.
    max_angle (float): The maximum angle in degrees.

    Returns:
    float: The corresponding angle in degrees.
    """
    # Clamp the PWM to the specified range
    if pwm < min_pwm:
        pwm = min_pwm
    elif pwm > max_pwm:
        pwm = max_pwm

    # Linear interpolation to find the angle
    angle = min_angle + (pwm - min_pwm) * (max_angle - min_angle) / (max_pwm - min_pwm)
    return angle




#TO CONVERT TO DEGREES WHEN GIVEN MECHANISM
### atp = angle to pwm ###

def pflap_atp(angle):
    return angle_to_pwm(angle, min_angle=0, max_angle=30)

def sflap_atp(angle):
    return angle_to_pwm(angle, min_angle=0, max_angle=30)

def paileron_atp(angle):
    return angle_to_pwm(angle, min_angle=-40, max_angle=40)

def saileron_atp(angle):
    return angle_to_pwm(angle, min_angle=-40, max_angle=40)

def rudder_atp(angle):
    return angle_to_pwm(angle, min_angle=-40, max_angle=40)

def elevator_atp(angle):
    return angle_to_pwm(angle, min_angle=-45, max_angle=45)




# TO CONVERT TO DEGREES WHEN GIVEN PWM SIGNAL
### pta = pwm to angle ###

def pflap_pta(pwm):
    return pwm_to_angle(pwm, min_pwm=800, max_pwm=2500, min_angle=0, max_angle=30)

def sflap_pta(pwm):
    return pwm_to_angle(pwm, min_pwm=800, max_pwm=2500, min_angle=0, max_angle=30)

def paileron_pta(pwm):
    return pwm_to_angle(pwm, min_pwm=800, max_pwm=2500, min_angle=-40, max_angle=40)

def saileron_pta(pwm):
    return pwm_to_angle(pwm, min_pwm=800, max_pwm=2500, min_angle=-40, max_angle=40)

def rudder_pta(pwm):
    return pwm_to_angle(pwm, min_pwm=800, max_pwm=2500, min_angle=-40, max_angle=40)

def elevator_pta(pwm):
    return pwm_to_angle(pwm, min_pwm=800, max_pwm=2500, min_angle=-45, max_angle=45)

