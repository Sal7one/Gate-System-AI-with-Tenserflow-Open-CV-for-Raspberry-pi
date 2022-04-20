from time import sleep
import mask as Maskdetector
import detect as HealthBardetector
import face as Facedetector
import temp as Tempdetector


def sendLCDMesssage(message):
    print(message)

while True:
    # -------- Phase 1 Mask detection  ---------

    # LCD Put mask on
    sendLCDMesssage("Welcome, please put your mask on")

    # Detect mask 
    Maskdetector.startMaskDetect()

    # -------- Phase 2 Face of person and Tawaklna comparison ---------
    sendLCDMesssage("Please, remove your mask ")
    sleep(3)

    sendLCDMesssage("Look at the Camera foucusing your face exactly infront")
    sleep(4)
    
    if Facedetector.start():
           #--------------- Phase 3 Start ----------------
        sleep(1)
        sendLCDMesssage("Please Show Tawakkalna status")
        sleep(2)
        
        # Model Name, Camera ID, Width, Height, Num of CPU Cores, run the model on 
        HealthBardetector.startHealthBarDetect("models/barmodel.tflite", 0, 640, 480, 4, False)
        
       #--------------- Phase 4 Start ----------------
        sleep(1)
        sendLCDMesssage("Please put your hand infront of the temperature sensor")
        sleep(2)

        if Tempdetector.start():
            sendLCDMesssage("Granted Enetry")
        else:
            sendLCDMesssage("Sorry something is wrong")

    else:
        sendLCDMesssage("Sorry something is wrong")
        
    sleep(15) # for next user