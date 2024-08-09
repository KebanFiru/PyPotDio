int Data[2];
int mainData[3];

void setup() {
  Serial.begin(9600);

}

void loop() {
  int data = analogRead(A3); //This is the pin connect to middle terminal of pot
  int newData = map(data, 0,1020,0,50); 
 for (int i = 0; i < 3; i++) {
     mainData[i] = newData;
     if (i == 3) {
      i = 0;
    }
    Data[0] = mainData[1];
    Data[1] = mainData[2];
    if(Data[0] < Data[1]){
      Serial.println(newData); }
    else if (Data[0] > Data[1]){
      Serial.println(newData);
  }
  
  
}}
  
