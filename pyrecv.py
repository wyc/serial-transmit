#!/usr/bin/python

from sys import argv

def waitPreamble(ser):
    i = 0
    while True:
        b = ord(ser.read(1))
        if b == 0x55:
            i = i + 1
        elif b == 0x0 and i > 100:
            print("Preamble Received and Verified")
            return True
        else:
            print("Bad Data: 0x%x" % ord(ser.read(1)))

def isPostamble(postfix):
    if len(postfix) < 101:
        return False
    i = 0
    for b in postfix:
        if b == 0x55:
            if i == 100:
                print("Postamble Received and Verified")
                return True
            elif i > 0:
                i = i + 1
        elif b == 0x0:
            if i == 0:
                i = i + 1
            else:
                return False
        else:
            return False

def updatePostfix(postfix, ba):
    wr = []
    extra = (len(postfix) + len(ba)) - 101
    if extra > 0:
        for i in range(0, extra):
            wr.append(postfix.pop(0))
    postfix.extend(ba)
    return wr

import serial

ser = serial.Serial('/dev/ttyUSB0', baudrate=700000)
print(ser.name, ": RX")

waitPreamble(ser)

outpath = argv[1]

f = open(outpath, "w")
postfix = []
print("Receiving File")
while True:
    ca = ser.read(1)
    ba = ca
    wr = updatePostfix(postfix, ba) 
    if isPostamble(postfix):
        break
    wr = ''.join(list(map(chr, wr)))
    f.write(wr)

