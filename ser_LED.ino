#include <EEPROM.h>

const int ledPin = 2; 
const int EEPROM_SIZE = 2;
const int THROTTLE_ADDR = 0;
const int DIRECTION_ADDR = 1;
char command;

void setup()
{
  // Initialize serial communication at 9600 baud
  Serial.begin(9600);
  
  // Set the LED pin as output
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);  // Start with the LED off

  // Check if EEPROM is properly initialized
  if (!EEPROM.begin(EEPROM_SIZE)) 
  {
    Serial.println("Failed to initialize EEPROM");
    return;
  }

  // Store initial throttle and direction values
  int throttle = 50;  
  int direction = 1;  
  storeThrottleDirection(throttle, direction);

  Serial.println("Throttle and Direction saved to EEPROM.");
}

void loop() 
{
  if (Serial.available() > 0) 
  {
    command = Serial.read();  // Read the incoming byte

    // LED control based on commands
    if (command == 'o') 
    {
      digitalWrite(ledPin, HIGH);  // Turn on LED
      Serial.println("LED ON");
    }
    
    else if (command == 'x') 
    {
      digitalWrite(ledPin, LOW);  // Turn off LED
      Serial.println("LED OFF");
    }
  }
}

void storeThrottleDirection(int throttle, int direction) 
{
  throttle = constrain(throttle, 0, 100);  // Ensure throttle is between 0 and 100
  direction = constrain(direction, 1, 2);   // Ensure direction is 1 or 2 (CW or CCW)

  EEPROM.write(THROTTLE_ADDR, throttle);
  EEPROM.write(DIRECTION_ADDR, direction);
  EEPROM.commit();                  // Commit changes to EEPROM
}
