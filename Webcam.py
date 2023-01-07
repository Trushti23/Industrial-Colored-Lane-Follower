import cv2

cap=cv2.VideoCapture(0)

def getImg(display=True):
    _,img=cap.read()     
    img=img=cv2.resize(img,(480,240))
    #img=cv2.flip(img,-1)    for rpi camera setting
    if display:
        cv2.imshow('IMG',img)
    return img



########## Function used in MainRobotLane to release cam if q is pressed
def release():
    cap.release


if __name__ == '__main__':
    while True:
        img=getImg(True)
        ##FOLLOWING LINES NOT THERE IN MURTAZA's Code
        if cv2.waitKey(1)  == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows() 
    
    
