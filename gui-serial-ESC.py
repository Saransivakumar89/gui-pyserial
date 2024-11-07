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

# Connecting to the port
def connect():
    global ser
    selected_port = port_combobox.get()
    selected_baudrate = baudrate_combobox.get()
    if selected_port:
        if ser and ser.is_open:
            status_label.config(text=f"Already connected to {ser.portstr}")
        else:
            try:
                ser = serial.Serial(selected_port, baudrate=int(selected_baudrate), timeout=1)
                status_label.config(text=f"Connected to {selected_port} with baudrate {selected_baudrate}")
            except serial.SerialException as e:
                status_label.config(text=f"Error: {e}")
    else:
        status_label.config(text="No Port Selected")

# Disconnecting the port
def disconnect():
    global ser
    if ser and ser.is_open:
        ser.close()
        status_label.config(text=f"Disconnected from {ser.portstr}")
    else:
        status_label.config(text="No active connection to disconnect!")

# LED on
def turn_on_led():
    if ser and ser.is_open:
        ser.write(b'o')
        status_label.config(text="LED ON")
    else:
        status_label.config(text="Not connected to a serial port!")

# LED off
def turn_off_led():
    if ser and ser.is_open:
        ser.write(b'x')
        status_label.config(text="LED OFF")
    else:
        status_label.config(text="Not connected to a serial port!")

# Set baud rate
def set_baudrate():
    selected_baudrate = baudrate_combobox.get()
    status_label.config(text=f"Baudrate set to: {selected_baudrate}")

# Set throttle
def set_throttle():
    if ser and ser.is_open:
        throttle_value = throttle_slider.get()
        ser.write(f"t{throttle_value}".encode())  
        status_label.config(text=f"Throttle set to: {throttle_value}")
    else:
        status_label.config(text="No active connection! Unable to set throttle.")

# Set direction
def set_direction():
    if ser and ser.is_open:
        direction = 'CW' if direction_var.get() == 1 else 'CCW'
        ser.write(direction.encode())  
        status_label.config(text=f"Direction set to: {direction}")
    else:
        status_label.config(text="No active connection! Unable to set direction.")

# Create the window
root = tk.Tk()
root.title('GUI')
root.geometry("400x500")  

# Status label to display messages
status_label = tk.Label(root, text="", fg="red")
status_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Port Entry/Dropdown Box
port_combobox = ttk.Combobox(root, values=get_com_ports())
port_combobox.grid(row=1, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

# Connect & Disconnect Buttons
connect_button = tk.Button(root, text="Connect", command=connect)
connect_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

disconnect_button = tk.Button(root, text="Disconnect", command=disconnect)
disconnect_button.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Baudrate Entry/Dropdown Box & Button
baudrate_combobox = ttk.Combobox(root, values=baud_rates)
baudrate_combobox.set(9600)
baudrate_combobox.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

set_button = tk.Button(root, text="Set Baudrate", command=set_baudrate)
set_button.grid(row=4, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

# LED on/off Button
turn_on_button = tk.Button(root, text="Turn On LED", command=turn_on_led)
turn_on_button.grid(row=5, column=0, padx=10, pady=5, sticky="ew")

turn_off_button = tk.Button(root, text="Turn Off LED", command=turn_off_led)
turn_off_button.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

# Throttle Slider
throttle_label = tk.Label(root, text="Throttle")
throttle_label.grid(row=6, column=0, columnspan=2)
throttle_slider = tk.Scale(root, from_=0, to=100, orient="horizontal")
throttle_slider.grid(row=7, column=0, padx=10, pady=5, sticky="ew", columnspan=2)

throttle_set_button = tk.Button(root, text="Set Throttle", command=set_throttle)
throttle_set_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# Direction Radio Buttons
direction_var = tk.IntVar(value=1)
direction_label = tk.Label(root, text="Direction")
direction_label.grid(row=9, column=0, columnspan=2)
forward_button = tk.Radiobutton(root, text="CW", variable=direction_var, value=1)
forward_button.grid(row=10, column=0, padx=10, pady=5, sticky="w")
reverse_button = tk.Radiobutton(root, text="CCW", variable=direction_var, value=2)
reverse_button.grid(row=10, column=1, padx=10, pady=5, sticky="w")

direction_set_button = tk.Button(root, text="Set Direction", command=set_direction)
direction_set_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()




