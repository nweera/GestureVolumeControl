import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.5)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volRange=volume.GetVolumeRange()
print(volume.GetVolumeRange()) #prints (-65.25, 0.0, 0.03125)
volume.SetMasterVolumeLevel(-20.0, None)
minVol= volRange[0]
maxVol= volRange[1]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    l = detector.findPosition(img)
    if len(l) != 0:
        #print(l[4], l[8])

        x1, y1=l[4][1], l[4][2]
        x2, y2 = l[8][1], l[8][2]
        cx, cy = (x1 + x2)//2, (y1 + y2)//2
        cv2.circle(img, (x1, y1), 10,(255,0,255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10,(255,0,255), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (255,0,255), 3)
        cv2.circle(img, (cx, cy), 6, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2-x1, y2-y1)
        print(length)

        #hand range 15 - 200
        #volume range -65 - 0

        vol = np.interp(length, [15, 200], [minVol, maxVol])
        #print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length<50:
            cv2.circle(img, (cx, cy), 6, (0, 255, 0), cv2.FILLED)

    cTime= time.time()
    fps= 1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_ITALIC, 0.5, (255, 0, 0), 1)
    cv2.imshow("img", img)
    cv2.waitKey(1)