import serial
import time
from firebase import firebase

FBConn = firebase.FirebaseApplication('https://test-database-3176c.firebaseio.com/', None)


ser = serial.Serial()    #Create a serial port object
ser.baudrate = 115200    #Set the baud-rate to 115200 (make sure to use the same speed as the device you're connecting to!)
ser.port = "/dev/tty.usbmodem14402"        #Set the communications port
ser.open()               #Open the port

latestTemp = 0
latestKey = 0
lastKey = 0

while True:              #Loop forever
    
    result = FBConn.get('/tempData/', None)
    for keyID in result:
        print (keyID)
        print (result[keyID]['Start'])
        latestTemp = str(result[keyID]['Start']) #we need to convert to string to make the serial port happy
        latestKey = keyID
        
    if latestKey != lastKey:
        lastKey = latestKey
        ser.write(latestTemp.encode('UTF-8') + b"\n")
        
    time.sleep(5)      
    
ser.close() #Close serial port