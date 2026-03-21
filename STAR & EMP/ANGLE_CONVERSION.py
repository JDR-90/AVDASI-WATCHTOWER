
# Linear Enough Conversion, if not here use the dictionaries

def elevator_linear(angle):
    return int(1506 + (angle)*5.8372)

def rudder_linear(angle):
    return int(1605 + (angle)*5.5471)

def saileron_linear(angle):
    return int(1426.6 + (angle)*6.0912)

def sflap_linear(angle):
    return int(1184 + (angle)*3.8121)

def sflap_sensor_linear(angle):
    return int(242 + (angle)*0.3901)




# CONVERSION DICTIONARIES
sflap_dict = {
    0: 1188,
    5: 1204,
    10: 1218,
    15: 1236,
    20: 1261,
    25: 1286,
    30: 1298
}

saileron_dict = {
    -40:    1166,
    -35:    1226,
    -30:    1251,
    -25:    1280,
    -20:    1355,
    -15:    1341,
    -10:    1415,
    -5:     1393,
    0:      1411,
    5:      1462,
    10:     1479,
    15:     1533,
    20:     1560,
    25:     1566,
    30:     1615,
    35:     1641, 
    40:     1666
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
    -40:    0,
    -30:    0,
    -20:    0,
    -10:    0,
    0:      0,
    10:     0,
    20:     0,
    30:     0,
    40:     0
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
    -45:    1243,
    -40:    1272,
    -35:    1301,
    -30:    1330,
    -25:    1360,
    -20:    1389,
    -15:    1418,
    -10:    1447,
    -5:     1476,
    0:      1506,
    5:      1535,
    10:     1564,
    15:     1593,
    20:     1622,
    25:     1651,
    30:     1681,
    35:     1710,
    40:     1739,
    45:     1768
}



def sflap_deflection_get(item):
    return sflap_dict.get(item, 1183)

def sail_deflection_get(item):
    return saileron_dict.get(item, 1183)

def pflap_deflection_get(item):
    return pflap_dict.get(item, 1183)

def pail_deflection_get(item):
    return paileron_dict.get(item, 1183)

def rudder_deflection_get(item):
    return rudder_dict.get(item, 1605)

def elevator_deflection_get(item):
    return elevator_dict.get(item, 1506)