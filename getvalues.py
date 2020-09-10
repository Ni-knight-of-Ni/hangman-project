import serial
import time
from firebase import firebase



FBConn = firebase.FirebaseApplication('https://jbnni-51f87.firebaseio.com/',None)

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM4"
#ser.open() # mircrbit skal være tilsluttet...

MRKeyID = 0
MRKloss = 0
CheckID = 1

while True:
    myGetResults = FBConn.get('winlossxxx',None)
    
    for keyID in myGetResults:
        if int(myGetResults[keyID] > MRKloss):
            MRKloss =int(myGetResults[keyID])
            MRKeyID = myGetResults[keyID]
        
        microbitdata = str(myGetResults[keyID])
        
    
        if CheckID == MRKeyID:
           # print(microbitdata)
           # print(1)
            time.sleep(3)
        else :
        
            ser.write(microbitdata.encode('UTF-8') + b"\n")
            #print(1)
            #print(microbitdata)
            
            CheckID = MRKeyID
            time.sleep(20)
                
        
        #ser.write(microbitdata.encode('UTF-8') + b"\n")
    #print(microbitdata)
    


#ser.close 