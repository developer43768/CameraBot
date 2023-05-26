import cv2
import FaceLibrary
import ScreenPainter
import Communication
import threading
################################
wCam, hCam = 1280, 720
################################
 
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = FaceLibrary.FaceDetector()

database = Communication.Database()

a = 4


def comm():
    while True:
        database.GetDatabase()
        database.ConnectionControl()

def faceTrack():
    cntrl = 0
    while True:
        if(database.robotMode == '4' and database.robotOnline == 1):
            if(cntrl == 0):
                wCam , hCam = 1280,720
                cap.set(3,wCam)
                cap.set(4,hCam)
                cntrl = 1

            success, img = cap.read()
            faces = detector.detect_faces(img)
            img = detector.draw_faces(faces=faces,image=img)
            faceDatas = detector.CalculateFace(img) #  [0]: Destination     [1]: Face Area     [2]:Results
            ScreenPainter.putFps(img)
            cv2.imshow("Img", img)
            key = cv2.waitKey(1)

        elif(database.robotMode == '4' and database.robotOnline == 0):
            cv2.destroyAllWindows()
            cntrl = 0

                
face_trackThread = threading.Thread(target=faceTrack, daemon=True).start()
commThread = threading.Thread(target = comm, daemon=True).start()


while True:
    print("Connect Button : ",database.connectButton)
    print("Robot is Online : ",database.robotOnline)
    print("Robot Mode : ",database.robotMode)

