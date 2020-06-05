# midicontrol2
A little code to convert potentiometers datas from an Arduino into valid CC midi signals.

You need to respect the syntax of the serial printing by the arduino. For example, my code will take the input from the A1 pin, and call it pot1, and then print its reading everytime it's different like this : "pot1:50" , 50 being the value.


The python script will ask you what midi port to use, and then what serial port to read from. 
Then you can assign the signals in your favorite software. (if it's ableton be sure to activate the port as 'Remote' in the midi settings).
