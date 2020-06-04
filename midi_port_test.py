# TESTING THE DIALOG FOR MIDI PORT

import rtmidi_python as rtmidi
import serial
import time

midi_out = rtmidi.MidiOut(b'out')

ports_names = []

port_no = ''
number_of_ports = 0

while number_of_ports < 20:
    try:
        ports_names.append(midi_out.ports[number_of_ports])
    except:
        break
    number_of_ports += 1

print("Which midi port would you like to chose ? ")

while port_no is str():
    for i, port_name in enumerate(ports_names):
        print(i, ' : ', port_name)
    try:
        print("Enter the number associated with a midi port.")
        port_no = int(input())
    except:
        print("Incorrect Entry.")
        continue

print ("Using port: ", midi_out.ports[port_no])

midi_out.open_port(port_no)