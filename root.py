import rtmidi_python as rtmidi
import serial
import time
import serial.tools.list_ports
from tkinter import *

root = Tk(screenName="Midi Control 2")

var_choice = StringVar()

serials = list(serial.tools.list_ports.comports())

serial_list = Listbox(root)
serial_list.pack(padx=15, pady=15)


for i, ser in enumerate(serials):
    serialport = str(ser)
    serialport = serialport.split(' ')
    serialport = ser[0]
    serial_list.insert(END, serialport)
    # Radiobutton(root, text=serialport, variable=var_choice, value=serialport).pack()

# serialport = str(serials[serial_index])
# serialport = serialport.split(' ')
# serialport = serialport[0]

root.mainloop()

