void setup() {
  Serial.begin(9600);
}

void loop() {
  int data = analogRead(A3);
  int newData = map(data, 0,1023,0,100);
  Serial.println(newData);
}
