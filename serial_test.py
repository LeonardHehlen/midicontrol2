# TESTING THE DIALOG FOR SERIAL PORT

import serial.tools.list_ports

#SERIAL PORT SETUP

serials = list(serial.tools.list_ports.comports())

serial_index = ''

while serial_index is str():
    print("Choose a serialport to read from.")
    for i, ser in enumerate(serials):
        print(i, ' : ', ser)   
    try:
        serial_index = int(input())
    except:
        print("Incorrect Entry.")
    
serialport = str(serials[serial_index])
serialport = serialport.split(' ')
serialport = serialport[0]

print("Using Serial Port : ", serialport)