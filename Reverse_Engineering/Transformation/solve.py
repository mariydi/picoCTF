# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

enc = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽"
dec = ''

for i in range(len(enc)):
    a = bin(ord(enc[i]))
    b = bin(ord(enc[i]) >> 8)
    c = chr(ord(enc[i]) >> 8)
    dec += chr(ord(enc[i]) >> 8)
    d = bin(ord(enc[i]) & 0b11111111)
    dec += (chr(ord(enc[i]) & 0b11111111))

print(dec)
