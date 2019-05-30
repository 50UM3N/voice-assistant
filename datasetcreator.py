import os
import cv2

cam = cv2.VideoCapture(0)
faceCascade=cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml') #cascade classifier
i=0
people = input("Enter the name of the persion : ")
os.mkdir('images/'+people)
while(True):
    img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        i=i+1
        cv2.imwrite("images/"+ people +"/"+ str(i) + ".jpg", gray[y:y+h,x:x+w])
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        cv2.waitKey(1)
    cv2.imshow('frame',img)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    if (i>50):
        break
cam.release()
cv2.destroyAllWindows()
