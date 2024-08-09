import serial.tools.list_ports
import serial
ports = list(serial.tools.list_ports.comports())

try:
    for p in ports:
        if "CH340" in p.description:
            com = p.device
            print("Connection Complished")
    arduino = serial.Serial()
    arduino.baudrate = 9600
    arduino.port = '%s'%(com)
except:
    print("Connection failed")