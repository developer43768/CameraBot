import cv2
import FaceLibrary
import ScreenPainter
import Communication

################################
wCam, hCam = 640, 480
################################
 
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = FaceLibrary.FaceDetector()

database = Communication.Database()

a = 4

while True:
    #Reading Database
    
    database.GetDatabase()
    database.ConnectionControl()

    #print("Connect Button : ",database.connectButton)
    #print("Robot is Online : ",database.robotOnline)
    #print("Robot Mode : ",database.robotMode)

    if(database.robotMode=='4' and database.robotOnline == 1):
        success, img = cap.read()
        faces = detector.detect_faces(img)
        img = detector.draw_faces(faces=faces,image=img)
        faceDatas = detector.CalculateFace(img) #  [0]: Destination     [1]: Face Area     [2]:Results
        ScreenPainter.putFps(img)
        cv2.imshow("Img", img)
        
    elif(database.robotMode == '4' and database.robotOnline == 0):
        cv2.destroyAllWindows()

    print("Face Area : ",faceDatas[1])
    print("Target : ",faceDatas[0])

    if(database.robotMode == '4' and database.robotOnline == 1):
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

