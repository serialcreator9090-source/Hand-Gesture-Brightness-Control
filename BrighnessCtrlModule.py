import cv2
import mediapipe as mp
import screen_brightness_control as sbc
import numpy as np


class HandDetector:

   
    def __init__(self, mode=False, maxHands=2,
                 detectionCon=0.5, trackCon=0.5):

        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )

        self.mpDraw = mp.solutions.drawing_utils
        self.lmList = []


    def findHands(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:

            for handLms in self.results.multi_hand_landmarks:

                if draw:
                    self.mpDraw.draw_landmarks(
                        img,
                        handLms,
                        self.mpHands.HAND_CONNECTIONS
                    )

        return img


    def distance(self, p1, p2):

        x1, y1 = p1
        x2, y2 = p2

        return np.sqrt(
            (x2 - x1) ** 2 +
            (y2 - y1) ** 2
        )


    def brightness_control(self, img, draw=True):

        if self.results.multi_hand_landmarks:

            handLms = self.results.multi_hand_landmarks[0]

            lmList = []

            
            h, w, c = img.shape

            for id, lm in enumerate(handLms.landmark):

                cx = int(lm.x * w)
                cy = int(lm.y * h)

                lmList.append((cx, cy))

            
            if len(lmList) >= 9:

                distance = self.distance(
                    lmList[4],
                    lmList[8]
                )

                brightness = np.interp(
                    distance,
                    [30, 200],
                    [0, 100]
                )

                sbc.set_brightness(int(brightness))

                if draw:

                    cv2.putText(
                        img,
                        f"Brightness: {int(brightness)}%",
                        (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (255, 0, 0),
                        2
                    )

        return img


def main():

    cap = cv2.VideoCapture(0)

    detector = HandDetector()

    while True:

        success, img = cap.read()

       
        if not success:
            break

        img = detector.findHands(img)

        img = detector.brightness_control(img)

        cv2.imshow("Image", img)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()