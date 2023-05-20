from makeblock import megapipro
from makeblock import megapi
from math import dist

def FollowFaceState(faceArea,p1x=0,p1y=0,p2x=0,p2y=0,):
    """Moves Camera if its necessary.

    Keyword arguments:
    p1x -- Mid Screen X (default 0)
    p1y -- Mid Screen Y (default 0)
    p2x -- Mid Face X (default 0)
    p2y -- Mid Face Y (default 0)
    """
    distan = dist((p1x,p1y),(p2x,p2y))
    if distan > 5:  #85
        if p1x > p2x:
            print("SOL")
            #Move Cam to Left
            #megPi.stepperMotorRun(leftRightStep,2000)
        else:
            print("SAG")
            #Move Cam to Right
            #megPi.stepperMotorRun(leftRightStep,-2000)
            
        if p1y > p2y:
            print("YUKARI")
            #Move Cam to Up
            #megPi.stepperMotorRun(leftRightStep,-2000)
        else:
            print("ASAGI")
            #Move Cam to Down
    if faceArea <= 450:
        print("Forward")
        # Move Cam to forward
    elif (450<faceArea) and (faceArea<=650):
        print('bekle')
        # Wait Cam
    elif faceArea > 650:
        print("Backward")
        # Move cam to backward

    print("Track Face")
    #print(faceArea)

def ResetState():
    print("Reset")


def ScanState():
    print("Scan")


def RemoteControlState():
    print("Remote Control")


