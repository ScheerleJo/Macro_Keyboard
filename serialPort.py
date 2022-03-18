import serial

serialString = "" # Used to hold data coming over UART
macroLayer = 0

serialPort = serial.Serial(port = "COM5", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)


#serialPort.open()

def keyFunctionLayer1(button):
    #print('Utility Layer')
    match button:
        case 1: print()
        case 2: print()
    

def keyFunctionLayer2(button):
    #print('Editing Layer')
    if button == False:
        print()

def keyFunctionLayer3(button):
    #print('Programming Layer')
    if button == False:
        print()

serialPort.write(b"This is the data sent \r\n");

while True:
     # Wait until there is data waiting in the serial buffer
    if(serialPort.in_waiting > 0):

        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()

        # Print the contents of the serial data
        print(serialString.decode('Ascii'))

        # Tell the device connected over the serial port that we recevied the data!
        # The b at the beginning is used to indicate bytes!
        serialPort.write(b"Thank you for sending data \r\n")






