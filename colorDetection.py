import cv2
import numpy as np
from collections import deque


bufferSize = 16   
pts = deque(maxlen = bufferSize)

blueLower = (90, 50, 50)
blueUpper = (130, 255, 255)

redLower = (0, 100, 100)
redUpper = (10, 255, 255)

greenLower = (36, 100, 100)
greenUpper = (86, 255, 255)


cap = cv2.VideoCapture(0)
cap.set(3 , 960) 
cap.set(4 , 480) 

secenek = input("Mavi icin 'b' , Yesil icin 'g' , Kirmizi icin 'r' 'yi tuslayin...")


if(secenek == "b"):
    while True:
        success , imgOriginal = cap.read()
        
        if success:
            blurred = cv2.GaussianBlur(imgOriginal ,(11,11) , 0)  
            hsv = cv2.cvtColor(blurred , cv2.COLOR_BGR2HSV)
            cv2.imshow("HSV IMAGE" , hsv)
        
        mask = cv2.inRange(hsv , blueLower , blueUpper)
        cv2.imshow("HSV IMAGE" , hsv)
        mask = cv2.erode(mask , None , iterations = 2)
        mask = cv2.dilate(mask , None , iterations = 2)
        cv2.imshow("Mask + Erozyon ve Genisleme",mask)
       
        (contours , _) = cv2.findContours(mask.copy() , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
        
        center = None 
        if(len(contours) > 0): 
            c = max(contours , key = cv2.contourArea)
           
            rect = cv2.minAreaRect(c)  
            ((x,y) , (width,height) , rotation) = rect
           
            s = "x:{}  ,  y:{}  ,  width:{}  ,  height:{}  ,  rotation:{}".format(np.round(x),np.round(y),np.round(width),np.round(height),np.round(rotation))
            x2 = int(x)-int(width)
            y2= int(y)-int(height)
            print(s)
            
            
            box = cv2.boxPoints(rect)
            box = np.int64(box)
            
            
            M = cv2.moments(c) 
            center = (int(M["m10"] / M["m00"]) , int(M["m01"] / M["m00"]))
            
            cv2.drawContours(imgOriginal , [box] , 0 , (0,255,255) , 2)  
           
            cv2.circle(imgOriginal , center , 5 , (255,0,255) , -1)
    
            cv2.putText(imgOriginal , s , (15,50) , cv2.FONT_HERSHEY_PLAIN , 1 , (255,255,255) , 2)
            cv2.putText(imgOriginal , "Mavi" , (x2,y2) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 1 ,(255,255,255), 2)
      
        pts.appendleft(center)
        for i in range(1 , len(pts)):
            if(pts[i-1] is None or pts[i] is None):  
                continue
            cv2.line(imgOriginal , pts[i-1] , pts[i] , (0,255,0) , 3)
        cv2.imshow("Orijinal Tespit",imgOriginal)
            
        if(cv2.waitKey(1) & 0xFF == ord("q")):
            cv2.destroyAllWindows()
            break 
elif(secenek == "g"):
    while True:
        success , imgOriginal = cap.read()
       
        if success:
            blurred = cv2.GaussianBlur(imgOriginal ,(11,11) , 0)  
            hsv = cv2.cvtColor(blurred , cv2.COLOR_BGR2HSV)
            cv2.imshow("HSV IMAGE" , hsv)
       
        mask = cv2.inRange(hsv , greenLower , greenUpper)
        cv2.imshow("HSV IMAGE" , hsv)
       
        mask = cv2.erode(mask , None , iterations = 2)
        mask = cv2.dilate(mask , None , iterations = 2)
        cv2.imshow("Mask + Erozyon ve Genisleme",mask)
        
        (contours , _) = cv2.findContours(mask.copy() , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
        
        center = None 
        if(len(contours) > 0): 
            c = max(contours , key = cv2.contourArea)
            
            rect = cv2.minAreaRect(c)  
            ((x,y) , (width,height) , rotation) = rect    
            
            s = "x:{}  ,  y:{}  ,  width:{}  ,  height:{}  ,  rotation:{}".format(np.round(x),np.round(y),np.round(width),np.round(height),np.round(rotation))
            x2 = int(x)-int(width)
            y2= int(y)-int(height)
            print(s)
            
            box = cv2.boxPoints(rect)
            box = np.int64(box) 
            M = cv2.moments(c) 
            center = (int(M["m10"] / M["m00"]) , int(M["m01"] / M["m00"]))
            
            cv2.drawContours(imgOriginal , [box] , 0 , (0,255,255) , 2) 
            cv2.circle(imgOriginal , center , 5 , (255,0,255) , -1)
            
           
            cv2.putText(imgOriginal , s , (15,50) , cv2.FONT_HERSHEY_PLAIN , 1 , (255,255,255) , 2)
            cv2.putText(imgOriginal , "Yesil" , (x2,y2) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 1 , (255,255,255), 2)
        pts.appendleft(center)
        for i in range(1 , len(pts)):
            if(pts[i-1] is None or pts[i] is None): 
                continue
            cv2.line(imgOriginal , pts[i-1] , pts[i] , (0,255,0) , 3) 
            
        cv2.imshow("Orijinal Tespit",imgOriginal)          
        if(cv2.waitKey(1) & 0xFF == ord("q")):
            cv2.destroyAllWindows()
            break 
        
elif(secenek == "r"):
    while True:
        success , imgOriginal = cap.read()
        
        if success:
            blurred = cv2.GaussianBlur(imgOriginal ,(11,11) , 0) 
            hsv = cv2.cvtColor(blurred , cv2.COLOR_BGR2HSV)
            cv2.imshow("HSV IMAGE" , hsv)
        
       
        mask = cv2.inRange(hsv , redLower , redUpper)
        cv2.imshow("HSV IMAGE" , hsv)
        
        mask = cv2.erode(mask , None , iterations = 2)
        mask = cv2.dilate(mask , None , iterations = 2)
        cv2.imshow("Mask + Erozyon ve Genisleme",mask)
        
        (contours , _) = cv2.findContours(mask.copy() , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
        
        center = None 
        if(len(contours) > 0): 
            c = max(contours , key = cv2.contourArea)
            
            rect = cv2.minAreaRect(c)  
            ((x,y) , (width,height) , rotation) = rect
            
            s = "x:{}  ,  y:{}  ,  width:{}  ,  height:{}  ,  rotation:{}".format(np.round(x),np.round(y),np.round(width),np.round(height),np.round(rotation))
            x2 = int(x)-int(width)
            y2= int(y)-int(height)
            print(s)
            
            box = cv2.boxPoints(rect)
            box = np.int64(box) 
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]) , int(M["m01"] / M["m00"]))
            
            cv2.drawContours(imgOriginal , [box] , 0 , (0,255,255) , 2) 
            cv2.circle(imgOriginal , center , 5 , (255,0,255) , -1)
            
            cv2.putText(imgOriginal , s , (15,50) , cv2.FONT_HERSHEY_PLAIN , 1 , (255,255,255) , 2)
            cv2.putText(imgOriginal , "Kirmizi" , (x2,y2) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 1 , (255,255,255), 2)
        pts.appendleft(center)
        for i in range(1 , len(pts)):
            if(pts[i-1] is None or pts[i] is None):  
                continue
            cv2.line(imgOriginal , pts[i-1] , pts[i] , (0,255,0) , 3) 
        cv2.imshow("Orijinal Tespit",imgOriginal)
            
        if(cv2.waitKey(1) & 0xFF == ord("q")):
            cv2.destroyAllWindows()
            break 
else:
    print("Gecersiz islem!!")       