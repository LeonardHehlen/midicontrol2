import rtmidi_python as rtmidi
import serial
import time
import serial.tools.list_ports

# MIDI PORT SETUP
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

with serial.Serial(serialport, 115200, timeout=1) as ser:
    while(True):

        line = ser.readline()
        line = line.decode("utf-8")
        line = line.strip('\n')
        line = line.strip('\r')
        vals = (line.split(':'))

        midicontrols = []
        nb_elts = 0
        with open("midisignals", "r+") as midisignal:
            for line in midisignal:
                line = line.strip('\n')
                line = line.split(":")
                for l in line:
                    nb_elts += 1
                    midicontrols.append(l)

        i = 0

        while i < nb_elts:
            i+=1
            midicontrols[i] = int(midicontrols[i])
            i+=1

        if vals[0] == 'pot1':
            try:
                vals[1] = int(vals[1])
                midi_out.send_message([0xB0, midicontrols[1], vals[1]])
                print("pot1: ", vals[1], "CC", midicontrols[1])
            except:
                print("couldn't send message from pot1")
        if vals[0] == 'pot2':
            try:
                vals[1] = int(vals[1])
                midi_out.send_message([0xB0, midicontrols[3], vals[1]])
                print("pot2: ", vals[1], "CC",  midicontrols[3])
            except:
                print("couldn't send message from pot2")
        if vals[0] == 'pot3':
            try:
                vals[1] = int(vals[1])
                midi_out.send_message([0xB0, midicontrols[5], vals[1]])
                print("pot3: ", vals[1], "CC",  midicontrols[5])
            except:
                print("couldn't send message from pot3")
        if vals[0] == 'pot4':
            try:
                vals[1] = int(vals[1])
                midi_out.send_message([0xB0, midicontrols[7], vals[1]])
                print("pot4: ", vals[1], "CC",  midicontrols[7])
            except:
                print("couldn't send message from pot4")
        if vals[0] == 'pot5':
            try:
                vals[1] = int(vals[1])
                midi_out.send_message([0xB0, midicontrols[9], vals[1]])
                print("pot5: ", vals[1], "CC",  midicontrols[9])
            except:
                print("couldn't send message from pot5")
        if vals[0] == 'pot6':
            try:
                vals[1] = int(vals[1])
                midi_out.send_message([0xB0, midicontrols[11], vals[1]])
                print("pot6: ", vals[1], "CC",  midicontrols[11])
            except:
                print("couldn't send message from pot6")
        if vals[0] == 'pot7':
            try:
                vals[1] = int(vals[1])
                midi_out.send_message([0xB0, midicontrols[13], vals[1]])
                print("pot7: ", vals[1], "CC",  midicontrols[13])
            except:
                print("couldn't send message from pot7")