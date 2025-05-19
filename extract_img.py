import os
import cv2

videos = os.listdir("assets")
i=0
for video in videos:
    if video.endswith(".MOV") or video.endswith(".MP4"):
        video_path = os.path.join("assets", video)
        vid = cv2.VideoCapture(video_path)
        ret = True
        while ret:
            try:
                ret, frame = vid.read()
                cv2.imwrite(f"Datasets/frame{i}.jpeg", frame)
                print(f"Wrote Frame {i}")
                i+=1
            except:
                continue