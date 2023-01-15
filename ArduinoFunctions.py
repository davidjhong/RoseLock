import serial 
import time

#Configurations for mechanical functions 
RelayOn  = "On"
RelayOff = "Off"

DoorStateAfterClose = False # True: Leave door closed after opening it or leave it open  
#initialpos = False # True: Open upon Startup else closed on startup 

serialPort = "/dev/ttyACM0"
baudrate = 9600 

SC = serial.Serial(serialPort,baudrate)
SC.timeout = 1 

def open_door():
    print("Door is locked \n")
    SC.write(RelayOn.encode())
    time.sleep(1)
    if DoorStateAfterClose == True:
        time.sleep(3)
        close_door()
        
def close_door():
    print("Door is unlocked \n")
    SC.write(RelayOff.encode())
    time.sleep(1)
