import serial

def read_eeprom():
   
    ser = serial.Serial('COM7', 9600, timeout=1)
      
    ser.write(b'r')

    response = ser.readline().decode('utf-8').strip()
    
    print(f"EEPROM values: {response}")

def read_direction():
    ser = serial.Serial('COM7', 9600, timeout=1)
    
    ser.write(b'r')
    
    response = ser.readline().decode('utf-8').strip()
    
    print(f"Direction from EEPROM: {response}")
    
    ser.close()

read_direction()    
read_eeprom()
