import cv2
import mediapipe as mp
import time

# function of the cv2 library that is associated with the selection of the video source (here 0 is the built in webcam source)


class handDetector():
    def __init__(self, mode=False, maxHands=2, model_complexity=1 ,detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.model_complexity = model_complexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode, self.maxHands, self.model_complexity, self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        self.lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, landmarks in enumerate(myHand.landmark):
                # print(id, landmarks)
                h, w, c = img.shape
                cX, cY = int(landmarks.x*w), int(landmarks.y*h)
                self.lmList.append([id, cX, cY])
                if draw:
                    cv2.circle(img, (cX, cY), 16, (25, 247, 244), cv2.FILLED)
        return self.lmList

    def fingersUp(self):
        fingers = []

        if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers
def main():
    cap = cv2.VideoCapture(0)
    prevTime = 0
    currTime = 0
    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[8])
        currTime = time.time()
        fps = 1 / (currTime - prevTime)
        prevTime = currTime

        cv2.putText(img, "FPS: " + str(int(fps)), (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
