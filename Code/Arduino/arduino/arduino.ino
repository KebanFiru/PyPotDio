void setup() {
  Serial.begin(9600);
}

void loop() {
  int data = analogRead(A3); //This is the pin connect to middle terminal of pot
  int newData = map(data, 0,1023,0,100); 
  Serial.println(newData);
}
