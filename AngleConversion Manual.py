


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

sflap_params = [5.6160660926e-05,8.5705196823e-01,1.7658431160e-02,
                -6.0160484923e-03,9.5075244130e-04,-4.9112877149e-05,
                -5.0943233713e-06,9.1466817602e-07,-5.1946004166e-08,
                7.4324542114e-10,4.6781397748e-11,-1.6757103770e-12,
                -3.3765479350e-14,2.9160587918e-15,-6.0885269589e-17,4.4381524774e-19
                ]

saileron_params = [-4.0962770823e-04,8.1251840378e-01,-5.1600455010e-04,
                   -6.5820013004e-06,-1.1213972753e-06,-5.9291513320e-08,
                   4.2588768639e-09,2.2583955816e-10,-7.6809145139e-12,
                   -4.1850622114e-13,7.0335097979e-15,4.0344959313e-16,
                   -3.1731484681e-18,-1.9453905935e-19,5.6028287506e-22,3.6953233769e-23
                   ]


elevator_params = [1.8998831113e-03,-1.0319109353e+00,4.2513469715e-04,
                   -9.9946524137e-06,-1.8310806018e-07,3.5032111180e-08,
                   6.9235594486e-10,-8.7817623681e-11,-9.3617143573e-13,
                   1.0905458119e-13,6.6686123139e-16,-7.2000172555e-17,
                   -2.3663388903e-19,2.4072793002e-20,3.3124793926e-23,-3.2065293596e-24
                   ]

rudder_params = [4.2576801672e-03,9.9528590563e-01,7.2048162396e-04,
                 8.1297148116e-07,-2.4610836082e-07,-4.1379935769e-09,
                 1.5270778022e-09,2.6500212131e-11,-2.7976588119e-12,
                 -5.5834665522e-14,2.5409590380e-15,5.6220834466e-17,
                 -1.1271798220e-18,-2.7215323899e-20,1.9631972666e-22,5.1021270507e-24
                 ]



rc_flaps = [1000, 9.642]
rc_normal = [1500, 4.7817]


def polynomial(parameters, x):
    return sum(coef * (x ** i) for i, coef in enumerate(parameters))

def linear(param, x): 
    return  param[0] + param[1] * x


def def_to_rc(deflection, rc_param, cs_param):
    return linear(rc_param, polynomial(cs_param, deflection))



while True:
    control_surface = input("Enter control surface (PF, PA, SF, SA, R, E): ").upper()
    angle = float(input("Enter deflection angle in degrees: "))

    if control_surface == "PF":
        rc_value = round(def_to_rc(angle, rc_flaps, pflap_params))
        print(f"Port Flap RC Value: {rc_value}")
        print()

    elif control_surface == "PA":
        rc_value = round(def_to_rc(angle, rc_normal, paileron_params))
        print(f"Port Aileron RC Value: {rc_value}")
        print()

    elif control_surface == "SF":
        rc_value = round(def_to_rc(angle, rc_flaps, sflap_params))
        print(f"Starboard Flap RC Value: {rc_value}")
        print()
    
    elif control_surface == "SA":
        rc_value = round(def_to_rc(angle, rc_normal, saileron_params))
        print(f"Starboard Aileron RC Value: {rc_value}")
        print()
    
    elif control_surface == "R":
        rc_value = round(def_to_rc(-1*angle, rc_normal, rudder_params))
        print(f"Rudder RC Value: {rc_value}")
        print()

    elif control_surface == "E":
        rc_value = round(def_to_rc(angle, rc_normal, elevator_params))
        print(f"Elevator RC Value: {rc_value}")
        print()

    else:
        print("Invalid control surface. Please enter PF, PA, SF, SA, R, or E.")
        continue