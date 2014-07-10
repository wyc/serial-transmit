#!/usr/bin/python

from sys import argv

def sendPreamble(ser):
    for i in range(0, 200):
        ser.write([0x55])
    ser.write([0x0])
    print("Preamble Transmitted")

def sendPostamble(ser):
    ser.write([0x0])
    for i in range(0, 200):
        ser.write([0x55])
    print("Postamble Transmitted")

def sendFile(ser, path):
    f = open(path, "rb")
    while True:
        c = f.read(2048)
        if len(c) > 0:
            ser.write(c)
        else:
            break
    print("File Transmitted")

import serial

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)# 115200)  # open first serial port
print(ser.name, ": TX")

path = argv[1]
sendPreamble(ser)
sendFile(ser, path)
sendPostamble(ser)

