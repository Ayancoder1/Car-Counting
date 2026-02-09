from ultralytics import YOLO
import cv2
import cvzone
import math

cap = cv2.VideoCapture("Project 1 - Car Counter\Video_1.mp4")

model = YOLO("../Yolo_Weights/yolov8l.pt")

classNames = ["person","bicycle","car","motorcycle","airplane","bus","train","truck","boat",
              "traffic light","fire hydrant","stop sign","parking meter","bench",
              "bird","cat","dog","horse","sheep","cow","elephant","bear","zebra","giraffe",
              "backpack","umbrella","handbag","tie","suitcase",
              "frisbee","skis","snowboard","sports ball","kite",
              "baseball bat","baseball glove","skateboard","surfboard","tennis racket",
              "bottle","wine glass","cup","fork","knife","spoon","bowl",
              "banana","apple","sandwich","orange","broccoli","carrot",
              "hot dog","pizza","donut","cake",
              "chair","couch","potted plant","bed","dining table",
              "toilet","tv","laptop","mouse","remote","keyboard","cell phone"]

mask = cv2.imread("Project 1 - Car Counter/mask.png")

line_y = 450   # Counting line (y-position)
offset = 15

totalCars = set()     # Store counted IDs

while True:
    success, img = cap.read()
    if not success:
        break

    # img = cv2.resize(img, (854, 480))
    imgRegion = cv2.bitwise_and(img, mask)

    results = model.track(imgRegion, persist=True, stream=True)   # YOLO tracking

    cv2.line(img, (0, line_y), (1280, line_y), (0, 0, 255), 3)     # Draw counting line (BGR),thickness

    for r in results:
        boxes = r.boxes
        if boxes.id is None:
            continue

        for box, track_id in zip(boxes, boxes.id):
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            w, h = x2 - x1, y2 - y1

            conf = round(float(box.conf[0]), 2)
            cls = int(box.cls[0])
            currentClass = classNames[cls]
            track_id = int(track_id)

            if currentClass == "car" and conf > 0.3:
                cx = x1 + w // 2  
                cy = y1 + h // 2

                cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2)       # Bounding box

                cvzone.putTextRect(img, f'ID {track_id}', (x1, y1 - 10), scale=0.6, thickness=1, offset=3)    # ID label

                cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)     # Center point

                if (line_y - offset) < cy < (line_y + offset):       # LINE CROSSING CHECK
                    if track_id not in totalCars:
                        totalCars.add(track_id)
                        cv2.line(img, (0, line_y), (1280, line_y), (0, 255, 0), 5)

    cvzone.putTextRect( img, f'Count: {len(totalCars)}', (20, 50), scale=1.5, thickness=3, offset=15, colorR=(255, 0, 255))   # Display count

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
