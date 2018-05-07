void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
}

void blink(int totalTime) {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(totalTime);
    digitalWrite(LED_BUILTIN, LOW);
    delay(totalTime); 
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i = 0; i < 2; i++) {
    blink(200);
  }
  
  blink(1000);
}
