from ultralytics import YOLO
import cv2
import os

model = YOLO("yolov8n.pt")
image_dir = "Datasets"
images = os.listdir(image_dir)


for image in images:
    img = cv2.imread(os.path.join(image_dir, image))
    results = model(img)
    for result in results:
        for boxes in result.boxes.numpy():
            if len(boxes) == 1 and int(boxes.cls[0]) == 0 and boxes.conf>0.80:
                x1,y1,x2,y2 = boxes.xyxy[0]
                x,y,w,h = boxes.xywhn[0]
                print(0, x, y, w, h)
                x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)
                img = cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,200), 5)
                cv2.imshow("predictions", img)
                cv2.waitKey(100)
cv2.destroyAllWindows()

