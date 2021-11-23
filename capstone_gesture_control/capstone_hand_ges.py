import cv2
import time
import os
from . import HandTrackingModule as htm
import winsound
import pyttsx3

# import datetime

def handgesture():
    wCam, hCam = 640, 480

    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)

    # folderPath = "FingerImages"
    # myList = os.listdir(folderPath)
    # print(myList)
    # overlayList = []
    # for imPath in myList:
    #     image = cv2.imread(f'{folderPath}/{imPath}')
    #     # print(f'{folderPath}/{imPath}')
    #     overlayList.append(image)

    # print(len(overlayList))

    pTime = 0

    detector = htm.handDetector(detectionCon=0.75)

    tipIds = [4, 8, 12, 16, 20]
    cnt = 0;
    passcode = []

    text_speech = pyttsx3.init()

    #Sound
    # duration = 1750  # milliseconds
    # freq = 300  # Hz

    # start = datetime.datetime.now()

    while True:
        # cnt += 1
        success, img = cap.read()
        # img[0:200, 0:200] = overlayList[0]
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)

        if len(lmList) != 0:
            # if lmList[8][2] < lmList[6][2]:
            #     print('Index finger open')
            fingers = []

            # For thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # for remaining 4 fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # print(fingers)
            totalFingers = fingers.count(1)
            print(totalFingers)

            # h, w, c = overlayList[totalFingers-1].shape
            # img[0:h, 0:w] = overlayList[totalFingers - 1]
            
            # curr = datetime.datetime.now()
            if cnt % 50 == 0:

                # winsound.Beep(freq, duration)
                text_speech.say("Next")
                text_speech.runAndWait()

                # cv2.rectangle(img, (20, 225), (470, 425), (0, 255, 0), cv2.FILLED)
                # cv2.putText(img, "NEXT", (45, 375), cv2.FONT_HERSHEY_PLAIN,
                #         10, (255, 0, 0), 25)
                passcode.append(totalFingers)
                if len(passcode) == 6:
                    print(passcode)

                    return passcode

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
        #             3, (255, 0, 0), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)
        cnt += 1