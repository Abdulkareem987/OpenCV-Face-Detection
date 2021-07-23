import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in faces:

        # Blue Rectangle around the face
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        
    #Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

# When everything is done, release the capture
cap.realese()
cv2.destroyAllWindows()
