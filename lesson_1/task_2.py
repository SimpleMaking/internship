def int32_to_ip(int32):
    IP_adress = list()
    shift = 24
    for value in range(4):
        IP_adress.append((int32 >> shift) & 0xFF)
        if value != 3:
            IP_adress.append(".") 
        shift -= 8
    ip_adress = str()
    for value in IP_adress:
        ip_adress += str(value)
    return ip_adress

assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
