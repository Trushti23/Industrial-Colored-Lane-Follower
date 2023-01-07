import cv2
import numpy as np

def thresholding(img):                      ########ENTER HSV VALUES HERE
    imgHsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowwerWhite = np.array([0, 101, 114])
    upperWhite = np.array([255, 255, 255])
    mask = cv2.inRange(imgHsv, lowwerWhite, upperWhite)
    cv2.imshow('mask',mask)
    return mask

def getContours(imgThresh, img):
    contours, hierarchy = cv2.findContours(imgThresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    biggest=max(contours,key=cv2.contourArea)
    x,y,w,h=cv2.boundingRect(biggest)
    cx=x + w//2
    cy=y + h//2
    cv2.drawContours(img,biggest,-1,(0,255,0),2)
    cv2.circle(img,(cx,cy),4,(0,0,255),cv2.FILLED)