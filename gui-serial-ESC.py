import tkinter as tk
from tkinter import ttk
import serial
import serial.tools.list_ports

ser = None

baud_rates = [9600, 19200, 38400, 57600, 115200]

# Available Ports
def get_com_ports():
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]

#Connecting to the port
def connect():
    global ser
    selected_port = port_combobox.get()
    selected_baudrate = baudrate_combobox.get()  
    if selected_port:
        if ser and ser.is_open:
            print(f"Already connected to {ser.portstr}")
        else:
            try:
                ser = serial.Serial(selected_port, baudrate=int(selected_baudrate), timeout=1)
                print(f"Connected to {selected_port} with baudrate {selected_baudrate}")
            except serial.SerialException as e:
                print(f"Error: {e}")
    else:
        print("No Port Selected")

#Disconnects the Ports
def disconnect():
    global ser
    if ser and ser.is_open:
        ser.close()
        print(f"Disconnected from {ser.portstr}")
    else:
        print("No active connection to disconnect!")

#LED on
def turn_on_led():
    if ser and ser.is_open:
        ser.write(b'o')  
        print("LED ON")
    else:
        print("Not connected to a serial port!")

#LED off
def turn_off_led():
    if ser and ser.is_open:
        ser.write(b'x') 
        print("LED OFF")
    else:
        print("Not connected to a serial port!")

def set_baudrate():
    selected_baudrate = baudrate_combobox.get()  
    print(f"Baudrate set to: {selected_baudrate}")
    
#Creates the Window
root = tk.Tk()
root.title('Reflex Drive')
root.geometry("350x250")  

#Port Entry/Dropdown Box
port_combobox = ttk.Combobox(root, values=get_com_ports())
port_combobox.grid(row=0, column=0, padx=15, pady=10, sticky="ew", columnspan=2)

#Connect & Disconnect Buttons
connect_button = tk.Button(root, text="Connect", command=connect)
connect_button.grid(row=1, column=0, padx=15, pady=5, sticky="ew")

disconnect_button = tk.Button(root, text="Disconnect", command=disconnect)
disconnect_button.grid(row=1, column=1, padx=15, pady=5, sticky="ew")

#Baudrate Entry/Dropdown Box & Button
baudrate_combobox = ttk.Combobox(root, values=baud_rates)
baudrate_combobox.set(115200)  
baudrate_combobox.grid(row=2, column=0, padx=15, pady=10, sticky="ew", columnspan=2)


set_button = tk.Button(root, text="Set Baudrate", command=set_baudrate)
set_button.grid(row=3, column=0, padx=15, pady=10, sticky="ew", columnspan=2)

#LED on/off Button
turn_on_button = tk.Button(root, text="Turn On LED", command=turn_on_led)
turn_on_button.grid(row=4, column=0, padx=15, pady=5, sticky="ew")

turn_off_button = tk.Button(root, text="Turn Off LED", command=turn_off_led)
turn_off_button.grid(row=4, column=1, padx=15, pady=5, sticky="ew")


root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()



