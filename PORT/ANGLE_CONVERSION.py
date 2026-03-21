
# Linear Enough Conversion, if not here use the dictionaries

def elevator_linear(angle):
    return int(1506 + (angle)*5.8372)

def rudder_linear(angle):
    return int(1605 + (angle)*5.5471)


def pflap_linear(angle):
    return int(1113.7 +(angle)*11.965)

def pflap_sensor_linear(angle):
    return int(-73.578 + (angle)*0.3968)

# CONVERSION DICTIONARIES
sflap_dict = {
    0: 1183,
    5: 1190,
    10: 1218,
    15: 1245,
    20: 1259,
    25: 1274,
    30: 1293
}

saileron_dict = {
    -40:    1285,
    -30:    1333,
    -20:    1355,
    -10:    1415,
    0:      1460,
    10:     1512,
    20:     1579,
    30:     1600,
    40:     1645
}



pflap_dict = {
    0:      0,
    5:      0,
    10:     0,
    15:     0,
    20:     0,
    25:     0,
    30:     0
}

paileron_dict = {
    -40:    1503,
    -35:    1479,
    -30:    1466,
    -25:    1435,
    -20:    1415,
    -15:    1400,
    -10:    1370,
    -5:     1349,
    0:      1330,
    5:      1303,
    10:     1269,
    15:     1246,
    20:     1221,
    25:     1178,
    30:     1149,
    35:     1105,
    40:     1019
}


rudder_dict = {
    -40:    1390,
    -35:    1423,
    -30:    1448,
    -25:    1470,
    -20:    1501,
    -15:    1530,
    -10:    1545,
    -5:     1570,
    0:      1605,
    5:      1626,
    10:     1670,
    15:     1703,
    20:     1725,
    25:     1750,
    30:     1774,
    35:     1800,
    40:     1840
}

elevator_dict = {
    -45:    1258,
    -40:    1274,
    -35:    1302,
    -30:    1325,
    -25:    1363,
    -20:    1388,
    -15:    1426,
    -10:    1455,
    -5:     1485,
    0:      1506,
    5:      1536,
    10:     1563,
    15:     1600,
    20:     1618,
    25:     1652,
    30:     1687,
    35:     1711,
    40:     1746,
    45:     1777
}



def sflap_deflection_get(item):
    return sflap_dict.get(item, 1183)

def sail_deflection_get(item):
    return saileron_dict.get(item, 1183)

def pflap_deflection_get(item):
    return pflap_dict.get(item, 1183)

def pail_deflection_get(item):
    return paileron_dict.get(item, 1330)

def rudder_deflection_get(item):
    return rudder_dict.get(item, 1605)

def elevator_deflection_get(item):
    return elevator_dict.get(item, 1506)