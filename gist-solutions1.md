void setup() {
  // Initialize the LED pin as an output
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // Turn the LED on (HIGH is the voltage level)
  digitalWrite(LED_BUILTIN, HIGH);
  // Wait for a second
  delay(1000);
  // Turn the LED off by making the voltage LOW
  digitalWrite(LED_BUILTIN, LOW);
  // Wait for a second
  delay(1000);
}
