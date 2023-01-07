#unchanged
import cv2
import numpy as np
from motor import move, stop
import time
sensors=3
threshold = 0.2           
cap=cv2.VideoCapture(0)
weights= [-30,-15,0,15,30]
#weights= [-45,-35-25,-15,0,15,25,35,45]   FOR 5


##################################### PID PARAMETERS ######################################################


def thresholding(img):                      ########ENTER HSV VALUES HERE
    imgHsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowwerWhite = np.array([0, 101, 114])
    upperWhite = np.array([255, 255, 255])
    mask = cv2.inRange(imgHsv, lowwerWhite, upperWhite)
    cv2.imshow('mask',mask)
    return mask

# def getContours(imgThresh, img):
#     contours, hierarchy = cv2.findContours(imgThresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#     if len(contours)>0:
#         contours=max(contours,key=cv2.contourArea)
#         x,y,w,h=cv2.boundingRect(contours)
#         cx=x + w//2
#         cy=y + h//2
#         cv2.drawContours(img,contours,-1,(0,255,0),2)
#         cv2.circle(img,(cx,cy),4,(0,0,255),cv2.FILLED)

def getSensorOutput(imgThresh,sensors):
    imgs=np.hsplit(imgThresh,sensors)
    totalPixels = (img.shape[1]//sensors)*img.shape[0]
    senOut =[]
    for x, im in enumerate(imgs):
        pixelCount=cv2.countNonZero(im)
        if pixelCount>threshold*totalPixels:
            senOut.append(1)
        else:
            senOut.append(0)
        #cv2.imshow(str(x),im) 
    print(senOut)
    return senOut

def sendCommands(senOut):
    ## negative for left
    if   senOut== [0,1,0]: curve = weights[2]
    elif senOut== [1,0,0]: curve = weights[0]
    elif senOut== [0,0,1]: curve = weights[4]
    elif senOut== [1,1,0]: curve = weights[1]
    elif senOut== [0,1,1]: curve = weights[3]
    else: curve = weights[2]
    return curve




lastError=0
while True:
    _,img=cap.read()     
    img=img=cv2.resize(img,(960,240))
    #img=img=cv2.resize(img,(810,480))

    img=cv2.flip(img,-1)    #for rpi camera setting
    imgThresh = thresholding(img)
    #getContours(imgThresh,img)
    senOut = getSensorOutput(imgThresh,sensors)
    error = sendCommands(senOut)
    move(error,lastError)
    lastError=error
    








    
    cv2.imshow('IMG',img)
    if cv2.waitKey(1)  == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
