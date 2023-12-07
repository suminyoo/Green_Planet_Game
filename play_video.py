from imutils.video import VideoStream

import cv2
import pygame
import time
from pathlib import Path

def play_video():
    prev_time = 0
    FPS = 1

    # loop over the frames from the video stream
    SCRIPT_DIR = Path(__file__).parent
    video_file = SCRIPT_DIR/'video/ClimateChangeVideo.mp4'
    cap = cv2.VideoCapture(str(video_file))
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # 또는 cap.get(3)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # 또는 cap.get(4)
    fps = cap.get(cv2.CAP_PROP_FPS) # 또는 cap.get(5)
    print('프레임 너비: %d, 프레임 높이: %d, 초당 프레임 수: %d' %(width, height, fps))
    
        
    music_file = SCRIPT_DIR/'bgm/ClimateChangeVideo.wav'

    pygame.mixer.init()
    pygame.mixer.music.load(str(music_file))
    pygame.mixer.music.play()
    
    while cap.isOpened(): # cap 정상동작 확인
        ret, f = cap.read()
        f = cv2.resize(f, dsize=(2500, 1400) )
        text = "If you want to skip the video, press '0'"
        cv2.putText(f, text, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)
        
        current_time = time.time() - prev_time

        if (ret is True) and (current_time > 1./ FPS) :
            prev_time = time.time()
            
        # 프레임이 올바르게 읽히면 ret은 True
        if not ret:
            print("프레임을 수신할 수 없습니다(스트림 끝?). 종료 중 ...")
            break
        cv2.imshow('Frame', f)
        if cv2.waitKey(6) == ord('0'):
            break
        
    cap.release()
    cv2.destroyAllWindows()