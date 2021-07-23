import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')

class Video(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret, frame = self.video.read()
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces:

        # Blue Rectangle around the face
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        
        ret, jpg = cv2.imencode('.jpg', frame)
        return jpg.tobytes()