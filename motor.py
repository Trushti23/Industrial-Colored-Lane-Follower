#import Rpi.GIPO as GPIO
from pickle import GLOBAL
import numpy as np


def leftForward():
    pass
def leftBackward():
    pass
def rightForward():
    pass
def rightBackward():
    pass

lasterror=0
def move(error,lastError):
    baseSpeed=15
    MAXWHEELSPEED=50
    Kp=0.04                            #baseSpeed=15
    Kd=0
    Ki=0
    PID=int(Kp*error + Kd*(error-lastError) + Ki*(error + lastError))
    
    
        
    
    print("LeftSpeed=  ",np.clip(baseSpeed + PID,0,MAXWHEELSPEED)) 
    print("RightSpeed= ",np.clip(baseSpeed - PID,0,MAXWHEELSPEED)) 
def stop():
    leftSpeed=0
    rightSpeed=0

