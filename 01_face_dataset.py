
import sys

import cv2
import os
import sqlite3

#database start
scholarid= sys.argv[1]

cwd=os.getcwd()
database = r"{0}\attendence.db".format(cwd)
conn = sqlite3.connect(database)
sql = "SELECT * FROM record WHERE scholarid = '{0}'".format(scholarid)
cur = conn.cursor()
cur.execute(sql)
id = cur.fetchall()

#//////////////////////////////////////////////////////////


size = 4
cam = cv2.VideoCapture(0)
cam.set(3, 1920)  # set video width
cam.set(4, 1080)  # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = id[0][0]

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0

while (True):

    ret, img = cam.read()
    im = cv2.flip(img, 1)  # flip video image vertically
    # mini = cv2.resize(im, (im.shape[1] // size, im.shape[0] // size))
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, scaleFactor=2, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

        cv2.imshow('video', img)

    k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30:  # Take 30 face sample and stop video
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")

cam.release()
cv2.destroyAllWindows()
os.system('python3 training.py ')