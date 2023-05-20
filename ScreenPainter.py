import cv2
import time


global pTime
pTime = 0

def putFps(img):
    global pTime
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,1, (255, 0, 0), 3)
    