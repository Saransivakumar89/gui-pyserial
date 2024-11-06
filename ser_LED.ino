
const int ledPin = 2;  
char command;
void setup() {
  // Initialize serial communication at 9600 baud
  Serial.begin(9600);
  
  // Set the LED pin as output
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);  // Start with the LED off
}

void loop() {
  
  if (Serial.available() > 0) {
   
    command = Serial.read();

   
    if (command == 'o') {
      digitalWrite(ledPin, HIGH);
      Serial.println("LED ON");
    }
    
    else if (command == 'x') {
      digitalWrite(ledPin, LOW);
      Serial.println("LED OFF");
    }
  }
}
