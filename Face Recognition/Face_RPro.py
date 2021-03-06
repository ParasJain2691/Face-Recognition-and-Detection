import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

face_cascade = cv2.CascadeClassifier(r'E:/My Projects/Face Recognition Project/env/Face D & R/Face Recognition/haarcascade_frontalface_default.xml')

skip=0
face_data = []
dataset_path = r'../env/Face D & R/Face Recognition/data/'
face_section = np.zeros((100,100,3))

file_name = input("Enter name of Person")

while True:
    ret,frame = cap.read()
    if ret == False:
        continue

    faces = face_cascade.detectMultiScale(frame,1.3,5)
    faces = sorted(faces,key= lambda f:f[2]*f[3])

    for face in faces[-1:]:
        x,y,w,h = face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        offset=10
        face_section = frame[y-offset:y+h+offset, x-offset:x+w+offset]
        try:
            face_section = cv2.resize(face_section,(100,100))
        except:
            pass
        skip+=1
        if skip%10==0:
            face_data.append(face_section)

    cv2.imshow("frame",frame)
    cv2.imshow("Face Section",face_section)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

face_data = np.asarray(face_data)
face_data = face_data.reshape((face_data.shape[0],-1))

np.save(dataset_path + file_name, face_data)
print("Data Successfully at" + dataset_path + file_name + '.npy')


cap.release()
cv2.destroyAllWindows()       