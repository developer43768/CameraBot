import cv2
import mediapipe as mp
import math

class FaceDetector:
    def __init__(self, min_detection_confidence=0.5):
        self.min_detection_confidence = min_detection_confidence
        self.mp_face_detection = mp.solutions.face_detection
        self.mp_face_mesh = mp.solutions.face_mesh
        self.mp_draw = mp.solutions.drawing_utils
        self.face_detection = self.mp_face_detection.FaceDetection(min_detection_confidence=min_detection_confidence)
        self.face_mesh = self.mp_face_mesh.FaceMesh()
        self.results = 0

    def detect_faces(self, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.results = self.face_detection.process(image_rgb)
        faces = []
        if self.results.detections:
            for detection in self.results.detections:
                bbox = detection.location_data.relative_bounding_box
                h, w, _ = image.shape
                x, y, width, height = int(bbox.xmin * w), int(bbox.ymin * h), int(bbox.width * w), int(bbox.height * h)
                faces.append((x, y, width, height))
        return faces

    def draw_faces(self, image, faces):
        for (x, y, width, height) in faces:
            cv2.rectangle(image, (x, y), (x+width, y+height), (0, 255, 0), 2)
        return image

    def CalculateFace(self,image):
        faceDatas = [0,0,0]
        h, w, c = image.shape
        imageMidX = int(w/2)
        imageMidY = int(h/2)

        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                bBox = detection.location_data.relative_bounding_box

                

                fp1minX = int(bBox.xmin * w)
                fp1minY = int(bBox.ymin *h)

                fp2X = fp1minX + int(bBox.width * w)
                fp2Y = fp1minY + int(bBox.height * h)

                midFaceX = int((fp1minX+fp2X)/2)
                midFaceY = int((fp1minY+fp2Y)/2)


                faceArea = abs((fp2X - fp1minX) * (fp2Y - fp1minY))
                faceArea /= 100
                
                faceDest = math.sqrt(((midFaceX-imageMidX)*(midFaceX-imageMidX))+((midFaceY-imageMidY)*(midFaceY-imageMidY)))
                faceDatas = [faceDest,faceArea]
                
                cv2.circle(image,(midFaceX,midFaceY),10,(0,0,255),-1) # Middle point of the face
                cv2.line(image,(imageMidX,imageMidY),(midFaceX,midFaceY),(0,255,255),10) # midScreen to Face Yellow Line

        cv2.circle(image,(imageMidX,imageMidY),13,(0,255,255),2) # midScreen Yellow Circle
        cv2.rectangle(image,(imageMidX-int(w/4),imageMidY-int(w/4)),(imageMidX+int(w/4),imageMidY+int(w/4)),(0,155,255),5)
        return faceDatas 

