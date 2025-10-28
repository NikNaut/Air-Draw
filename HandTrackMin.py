import cv2
import mediapipe as mp
import time

# function of the cv2 library that is associated with the selection of the video source (here 0 is the built in webcam source)
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(False, 3)
mpDraw = mp.solutions.drawing_utils


prevTime = 0
currTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, landmarks in enumerate(handLms.landmark):
                # print(id, landmarks)
                h, w, c = img.shape
                cX, cY = int(landmarks.x*w), int(landmarks.y*h)
                if id == 8:
                    cv2.circle(img, (cX, cY), 16, (25, 247, 244), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    currTime = time.time()
    fps = 1/(currTime-prevTime)
    prevTime = currTime

    cv2.putText(img, "FPS: " + str(int(fps)), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

