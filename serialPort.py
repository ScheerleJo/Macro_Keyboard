import serial
from pynput.keyboard import Key, Controller
import requests
keyboard = Controller()

serialString = "" # Used to hold data coming over UART
lastButton = 0;

serialPort = serial.Serial(port = "COM4", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

def keyFunctionLayer(button:str, lastbutton:int):
    print(button)
    #print('Utility Layer')
    #match button:
    #   case "1": 
    #      print("Case 1 was activated")
    #   case "2": 
    #       print("Case 2 was activated")
    #   case "Switch Klicked": 
    #       print("Switch was pressed")

    if button == "Switch Klicked":
        keyboard.press(Key.f20)
        keyboard.release(Key.f20)
        r = requests.get('https://localhost:8000/send?action')
    elif button == "System successfully booted":
        print('Ready to go!')
    elif int(button) > lastbutton:
        keyboard.press(Key.f19)
        keyboard.release(Key.f19)
        print("b: " + str(button) + " l: " + str(lastButton))
        lastbutton = int(button)
    
    elif int(button) < lastbutton:
        keyboard.press(Key.f18)
        keyboard.release(Key.f18)
        print("b: " + str(button) + " l: " + str(lastButton))
        lastbutton = int(button)

    return lastbutton


serialPort.write(b"This is the data sent \r\n");

while True:
     # Wait until there is data waiting in the serial buffer
    if(serialPort.in_waiting > 0):

        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()

        # Print the contents of the serial data
        #print(serialString.decode('Ascii').strip())
        lastButton = keyFunctionLayer(serialString.decode('Ascii').strip(), lastButton)

        # Tell the device connected over the serial port that we recevied the data!
        # The b at the beginning is used to indicate bytes!
        serialPort.write(b"Thank you for sending data \r\n")






