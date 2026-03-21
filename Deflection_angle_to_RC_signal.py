


pflap_params = [-9.6710858170e-03, 2.6272363898e+00, -3.0134032548e-01, 
                1.4220208576e-01, -3.1240847766e-02, 3.4612864217e-03, 
                -1.7648402488e-04, 1.1364371683e-06, 2.1312079948e-07, 
                -1.1639871031e-09, -3.7904220063e-10, 5.7592642523e-12, 
                1.6637617778e-13, 5.2836014428e-15, -4.4025171650e-16, 5.8712144287e-18
                ]


paileron_params = [3.1881706125e-04, -1.1439896083e+00, -2.8362869317e-03, 
                   -1.6534831286e-05,2.8477663046e-07, 9.8532443193e-08,
                   -2.9305495379e-09, -3.2558305753e-10, 6.0665934905e-12, 
                   5.5953041617e-13, -6.3902306684e-15, -5.1494109407e-16, 
                   3.2678489754e-18, 2.3990822915e-19, -6.4465282994e-22, -4.4334363956e-23,
                   ]





from scipy.optimize import fsolve

def calculate_deflection(params, x):
    return sum(coef * (x ** i) for i, coef in enumerate(params))

def get_rc_signal_from_deflection(params, target_deflection):
   

    func = lambda x: calculate_deflection(params, x) - target_deflection
    
    servo_angle_solution = fsolve(func, x0=0)[0]
    
    
    rc_signal = (10.151 * servo_angle_solution) + 1512.5
    
    return rc_signal, servo_angle_solution


print("--- Deflection to RC Signal Converter ---")
choice = input("Enter 'a' for Aileron or 'f' for Flaps: ").lower()
target_d = float(input("Enter desired Deflection Angle (degrees): "))

if choice == 'a':
    params = paileron_params
    name = "Aileron"
else:
    params = pflap_params
    name = "Flap"

signal, derived_servo_angle = get_rc_signal_from_deflection(params, target_d)

print(f"\n--- Results for {name} ---")
print(f"To achieve {target_d}° deflection:")
print(f"1. Move Servo to: {derived_servo_angle:.2f}°")
print(f"2. Output RC Signal: {signal:.2f}")

