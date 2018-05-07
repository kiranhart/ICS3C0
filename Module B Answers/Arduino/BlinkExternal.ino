//Which pin in the external LED connected to?
int externalLED = 10;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(externalLED, OUTPUT);
}

void blink(int led, int delaytime) {
  digitalWrite(led, HIGH);
  delay(delaytime);
  digitalWrite(led, LOW);
  delay(delaytime);
}

/**
 * If Sync is true, then the led and external led will blink together
 * Otherwise, they'll offset
 **/
void synced(boolean sync) {
  if (sync) {
    for (int i = 0; i < 2; i++) {
      digitalWrite(externalLED, HIGH);
      digitalWrite(LED_BUILTIN, HIGH);
      delay(200);
      digitalWrite(externalLED, LOW);
      digitalWrite(LED_BUILTIN, LOW);
      delay(200);
    }
    digitalWrite(externalLED, HIGH);
    digitalWrite(LED_BUILTIN, HIGH);
    delay(1000);
    digitalWrite(externalLED, LOW);
    digitalWrite(LED_BUILTIN, LOW);
    delay(1000);
  } else {
    for (int i = 0; i < 2; i++) {
      blink(LED_BUILTIN, 200);
      blink(externalLED, 1000);
    }
    blink(LED_BUILTIN, 500);
    blink(externalLED, 100);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  synced(false);
}
