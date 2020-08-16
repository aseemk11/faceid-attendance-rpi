import datetime

import cv2
import sqlite3
import numpy as np
import os
from sqlite3 import Error
import sys

#database start


cwd=os.getcwd()
database = r"{0}\attendence.db".format(cwd)
conn = sqlite3.connect(database)
cur = conn.cursor()
cur.execute("SELECT scholarid FROM record ")

data = cur.fetchall()
cur.execute("SELECT id FROM record ")
ids= cur.fetchall()

#recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('training/02.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = [0]

# names related to ids: example ==> Marcelo: id=1,  etc
names = data

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 1920) # set video widht
cam.set(4, 1080) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
# Create a woorksheet


now= datetime.datetime.now()
today=now.day
month=now.month
hour=now.hour
min=now.minute
time=str(now.strftime("%I:%M %p"))
timestampStr = str(now.strftime("%d-%m-%Y-%p"))

try:
  cur.execute("Alter table record  ADD COLUMN `{0}` VARCHAR(45) DEFAULT 'Absent'  ".format(timestampStr,))
except Error as e:
    print(e)
while True:

    ret, img =cam.read()
    img = cv2.flip(img, 1) # Flip vertically

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        id1=""

        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 100):
            print (id)
            id1 = names[id-1][0]
            print(id1)

            confidence = "  {0}%".format(round(100 - confidence))

            # Assign attendance
            cur.execute("UPDATE`record` SET `{0}` = '{2}' WHERE (`scholarid` = '{1}')".format(timestampStr,id1,time))
            #sheet.cell(row=str(id1), column=int(today)).value = "Present"
            conn.commit()
            
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img, str(id1), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    cv2.putText(img, str(time), (1400,200), font, 1, (255,255,0), 1)
    cv2.imshow('camera',img)

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")

cam.release()
cv2.destroyAllWindows()
os.system('python3 output.py')
