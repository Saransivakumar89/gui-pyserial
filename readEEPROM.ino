#include <EEPROM.h>

const int EEPROM_SIZE = 2;
const int THROTTLE_ADDR = 0;
const int DIRECTION_ADDR = 1;

void setup() 
{
  Serial.begin(9600);  
  if (!EEPROM.begin(EEPROM_SIZE)) 
  {
    Serial.println("Failed to initialize EEPROM");
    return;
  }
  int throttle = EEPROM.read(THROTTLE_ADDR);
  int direction = EEPROM.read(DIRECTION_ADDR);

  Serial.print("Throttle: ");
  Serial.println(throttle);

  Serial.print("Direction: ");
  if (direction == 1) 
  {
    Serial.println("Forward");
  }
  else if (direction == 2)
  {
    Serial.println("Reverse");
  }
  
  else 
  {
    Serial.println("Invalid Direction");
  }
}

void loop()
{
}
