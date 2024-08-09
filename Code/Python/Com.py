
#!Serial communication interface for prototype use USB library in original product

import serial.tools.list_ports
import serial
ports = list(serial.tools.list_ports.comports())

try:
    for p in ports:
        if "CH340" in p.description:
            com = p.device
    arduino = serial.Serial()
    arduino.baudrate = 9600
    arduino.port = '%s'%(com)
except:
    pass