import serial
import time
from firebase import firebase



FBConn = firebase.FirebaseApplication('https://jbnni-51f87.firebaseio.com/',None)

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM4"
ser.open() # mircrbit skal være tilsluttet...

MRKeyID = 0
MRKloss = 0


while True:
    myGetResults = FBConn.get('winlossxxx',None)
    
    for keyID in myGetResults:
        if int(myGetResults[keyID] > MRKloss):
            MRKloss =int(myGetResults[keyID])
            MRKeyID = myGetResults[keyID]
        
    microbitdata = str(myGetResults[keyID])
    print(microbitdata)
    ser.write(microbitdata.encode('UTF-8') + b"\n")
    
    time.sleep(20)

ser.close 