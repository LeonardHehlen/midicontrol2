# midicontrol2
A little code to convert potentiometers datas from an Arduino into valid CC midi signals.

You need to respect the syntax of the serial printing by the arduino. For example, my code will take the input from the A1 pin, and call it pot1, and then print its reading everytime it's different like this : "pot1:50" , 50 being the value.


The python script will ask you what midi port to use, and then what serial port to read from. 
Then you can assign the signals in your favorite software. (if it's ableton be sure to activate the port as 'Remote' in the midi settings).

Also, if there is any conflict with another machine, you can change the CC signals of any pot at any time, even if the program is running.
For that, simply edit the file "midisignals" accordingly to it's format : potX:Y (X being the pot's number, and Y the CC number.)
