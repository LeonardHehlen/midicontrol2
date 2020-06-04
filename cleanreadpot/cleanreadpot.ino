#define pot1 A1
#define pot2 A2
#define pot3 A3
#define pot4 A4
#define pot5 A5
#define pot6 A6
#define pot7 A7


char sep = ':';

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(pot1, INPUT);
  pinMode(pot2, INPUT);
  pinMode(pot3, INPUT);
  pinMode(pot4, INPUT);
  pinMode(pot5, INPUT);
  pinMode(pot6, INPUT);
  pinMode(pot7, INPUT);

}

int treshold = 1;

void loop() {
  // put your main code here, to run repeatedly:
  int pot1_read = analogRead(pot1);
  int pot2_read = analogRead(pot2);
  int pot3_read = analogRead(pot3);
  int pot4_read = analogRead(pot4);
  int pot5_read = analogRead(pot5);
  int pot6_read = analogRead(pot6);
  int pot7_read = analogRead(pot7);

  delay(2);
  
  if ((analogRead(pot1) < pot1_read-treshold) or (analogRead(pot1) > pot1_read+treshold)){

    Serial.print("pot1");
    Serial.print(sep);
    Serial.print(map(analogRead(pot1), 1, 1023, 0, 127));
    Serial.print('\n');
  }
//  if ((analogRead(pot2) < pot2_read-treshold) or (analogRead(pot2) > pot2_read+treshold)){
//
//    Serial.print("pot2");
//    Serial.print(sep);
//    Serial.print(map(analogRead(pot2), 1, 1023, 0, 127));
//    Serial.print('\n');
//  }
//  if ((analogRead(pot3) < pot3_read-treshold) or (analogRead(pot3) > pot3_read+treshold)){
//
//    Serial.print("pot3");
//    Serial.print(sep);
//    Serial.print(map(analogRead(pot3), 1, 1023, 0, 127));
//    Serial.print('\n');
//  }
//
//  if ((analogRead(pot4) < pot4_read-treshold) or (analogRead(pot4) > pot4_read+treshold)){
//
//    Serial.print("pot4");
//    Serial.print(sep);
//    Serial.print(map(analogRead(pot4), 1, 1023, 0, 127));
//    Serial.print('\n');
//  }
//
//  if ((analogRead(pot5) < pot5_read-treshold) or (analogRead(pot5) > pot5_read+treshold)){
//
//    Serial.print("pot5");
//    Serial.print(sep);
//    Serial.print(map(analogRead(pot5), 1, 1023, 0, 127));
//    Serial.print('\n');
//  }
//
//  if ((analogRead(pot6) < pot6_read-treshold) or (analogRead(pot6) > pot6_read+treshold)){
//
//    Serial.print("pot6");
//    Serial.print(sep);
//    Serial.print(map(analogRead(pot6), 1, 1023, 0, 127));
//    Serial.print('\n');
//  }
//  if ((analogRead(pot7) < pot7_read-treshold) or (analogRead(pot7) > pot7_read+treshold)){
//
//    Serial.print("pot7");
//    Serial.print(sep);
//    Serial.print(map(analogRead(pot7), 1, 1023, 0, 127));
//    Serial.print('\n');
//  }
}
