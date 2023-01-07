import cv2
from utlis import thresholding, getContours
def getLane(img):
    imgThresh=thresholding(img)
    getContours(imgThresh,img)













if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while True:
        success,img =cap.read()
        img=cv2.resize(img,(480,240))
        #img=cv2.flip(img,-1)    for rpi camera setting
        getLane(img)
        #cv2.imshow("vid",img)
        cv2.waitKey(1)
