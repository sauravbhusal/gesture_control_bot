import cv2
import mediapipe as mp
import time
capture = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
fingerCoordinates = [(8, 6), (12, 10), (16, 14), (20, 18)]
thumbCoordinates = (4, 2)
gesturestr= str(0)

while True:
    ret, frame = capture.read()
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    multiLandMarks = results.multi_hand_landmarks

    if multiLandMarks:
        for handLm in multiLandMarks:
            handPoints = []
            mpDraw.draw_landmarks(frame, handLm, mpHands.HAND_CONNECTIONS)

            for idx, lm in enumerate(handLm.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                handPoints.append((cx, cy))


        for point in handPoints:
            print(point)
            cv2.circle(frame, point, 5, (0, 255, 255), -1)


        upcount = 0
        for coordinates in fingerCoordinates:
            if handPoints[coordinates[1]][1] > handPoints[coordinates[0]][1]:
                upcount += 1
        if handPoints[thumbCoordinates[1]][0] < handPoints[thumbCoordinates[0]][0]:
            upcount +=1

        cv2.putText(frame, str(upcount), (100,150), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 5, (0, 0, 250), 3)

        if upcount>=1:
            file = open('jetbot_return.txt', 'w')
            if upcount == 1:
                file.write('8')
            elif upcount == 2:
                file.write('4')
            elif upcount == 3:
                file.write('6')
            elif upcount == 4:
                file.write('2')
            elif upcount == 5:
                file.write('1')
            file.close()

        else:
            file = open('jetbot_return.txt','w')
            file.write('0')
            file.close()
    else:
        file = open('jetbot_return.txt','w')
        file.write('0')
        file.close()
            
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break


capture.release()
cv2.destroyAllWindows()
