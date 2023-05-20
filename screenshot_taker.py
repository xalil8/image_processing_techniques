

import cv2 
import numpy as np
import pandas as pd 

def main():
    source_video_path = "demo.mp4"
    video_write = False
    shape_present = False
    threshold = 50000
    previous_count = 0
    frame_counter = 0
    count = 0
    paused = False
    video_saving_path = source_video_path[:len(source_video_path)-4:]+"_output.mp4"
    video_cap = cv2.VideoCapture(source_video_path)
    fps = video_cap.get(cv2.CAP_PROP_FPS)
    width, height = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    desired_fps = 35

    if video_write:
        video = cv2.VideoWriter(video_saving_path, cv2.VideoWriter_fourcc(*'mp4v') ,fps, (width,height))

    while True:
        # Read a frame from the video stream
        ret, frame = video_cap.read()
        if not ret:
            break
        
        frame_counter += 1
        #ADJUST FPS
        if frame_counter % 1 != 0:
            continue


        if not video_write:
            cv2.imshow('STACKED OUTPUT', frame)
            #cv2.imshow("ROI",frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
    
    cv2.imwrite("xalil.png",frame)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("code has started")
    main()
    print("done")