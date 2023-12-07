from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import sys
import numpy
import pygame
from pathlib import Path
from tkinter import *
import math

from game_manager import GM
gm = GM()

def distance (markerCenter_X, markerCenter_Y, EarthCenter_X, EarthCenter_Y):
        # 마커 중점좌표 X - 지구 중점좌표 X = 밑변 a
            a = markerCenter_X - EarthCenter_X
        # 마커 중점좌표 Y -  지구 중점좌표 Y = 밑변 b
            b = markerCenter_Y - EarthCenter_Y
        # 루트(밑변 a 제곱 + 밑변 b 제곱) = 빗변 c 의 길이
            c = math.sqrt((a * a) + (b * b))
            #print(c)
        # 빗변의 길이가 1보다 작으면 true, 아니면 false --> true 반환시 information 함수 호출해서 설명 출력
        # 1보다 작게할지 아니면 다른 숫자를 적용할지는 테스트 해서 숫자 알아내야 함
            if c < int(300):
                return True
            else:
                return False

def ArUco(num):
    gm.play_bgm()
    
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--type", type=str,
        default="DICT_ARUCO_ORIGINAL",
        help="type of ArUCo tag to detect")
    args = vars(ap.parse_args())

    # define names of each possible ArUco tag OpenCV supports
    ARUCO_DICT = {
        "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
        "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
        "DICT_4X4_250": cv2.aruco.DICT_4X4_250,
        "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
        "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
        "DICT_5X5_100": cv2.aruco.DICT_5X5_100,
        "DICT_5X5_250": cv2.aruco.DICT_5X5_250,
        "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
        "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
        "DICT_6X6_100": cv2.aruco.DICT_6X6_100,
        "DICT_6X6_250": cv2.aruco.DICT_6X6_250,
        "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
        "DICT_7X7_50": cv2.aruco.DICT_7X7_50,
        "DICT_7X7_100": cv2.aruco.DICT_7X7_100,
        "DICT_7X7_250": cv2.aruco.DICT_7X7_250,
        "DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
        "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
        "DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
        "DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
        "DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
        "DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
    }

    # verify that the supplied ArUCo tag exists and is supported by
    # OpenCV
    if ARUCO_DICT.get(args["type"], None) is None:
        print("[INFO] ArUCo tag of '{}' is not supported".format(args["type"]))
        sys.exit(0)

    # load the ArUCo dictionary and grab the ArUCo parameters
    print("[INFO] detecting '{}' tags...".format(args["type"]))
    arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[args["type"]])
    arucoParams = cv2.aruco.DetectorParameters_create()

    # initialize the video stream and allow the camera sensor to warm up
    print("[INFO] starting video stream...")
    #vs = VideoStream(src=0).start()
    vs = VideoStream(src=1).start()
    time.sleep(2.0)

    #image load - good
    SCRIPT_DIR = Path(__file__).parent
    
        
    tree = cv2.imread(str(SCRIPT_DIR/"img/tree_planting.png"), cv2.IMREAD_UNCHANGED)
    solar = cv2.imread(str(SCRIPT_DIR/"img/solar.png"), cv2.IMREAD_UNCHANGED)
    bus = cv2.imread(str(SCRIPT_DIR/"img/bus.png"), cv2.IMREAD_UNCHANGED)
    recup = cv2.imread(str(SCRIPT_DIR/"img/recup.png"), cv2.IMREAD_UNCHANGED)
    recycle = cv2.imread(str(SCRIPT_DIR/"img/recycle.png"), cv2.IMREAD_UNCHANGED)
    wind = cv2.imread(str(SCRIPT_DIR/"img/wind.png"), cv2.IMREAD_UNCHANGED)
    unplug = cv2.imread(str(SCRIPT_DIR/"img/unplug.png"), cv2.IMREAD_UNCHANGED)
    shopping_basket = cv2.imread(str(SCRIPT_DIR/"img/shpping_basket.png"), cv2.IMREAD_UNCHANGED)
    turn_off = cv2.imread(str(SCRIPT_DIR/"img/turn_off.png"), cv2.IMREAD_UNCHANGED)
    bike = cv2.imread(str(SCRIPT_DIR/"img/bike.png"), cv2.IMREAD_UNCHANGED)
    
    #image load - bad
    factory = cv2.imread(str(SCRIPT_DIR/"img/factory.png"), cv2.IMREAD_UNCHANGED)
    airC = cv2.imread(str(SCRIPT_DIR/"img/airC.png"), cv2.IMREAD_UNCHANGED)
    meat = cv2.imread(str(SCRIPT_DIR/"img/meat.png"), cv2.IMREAD_UNCHANGED)
    car = cv2.imread(str(SCRIPT_DIR/"img/car.png"), cv2.IMREAD_UNCHANGED)
    plastic_bag = cv2.imread(str(SCRIPT_DIR/"img/bag.png"), cv2.IMREAD_UNCHANGED)
    foodwaste = cv2.imread(str(SCRIPT_DIR/"img/foodwaste.png"), cv2.IMREAD_UNCHANGED)
    waste = cv2.imread(str(SCRIPT_DIR/"img/waste.png"), cv2.IMREAD_UNCHANGED)
    oil = cv2.imread(str(SCRIPT_DIR/"img/oil.png"), cv2.IMREAD_UNCHANGED)
    pesticide = cv2.imread(str(SCRIPT_DIR/"img/pesticide.png"), cv2.IMREAD_UNCHANGED)
    tree_cut = cv2.imread(str(SCRIPT_DIR/"img/tree_cut.png"), cv2.IMREAD_UNCHANGED)

    #image load - other
    start = cv2.imread(str(SCRIPT_DIR/"screen_img/start.png"), cv2.IMREAD_UNCHANGED)
    help = cv2.imread(str(SCRIPT_DIR/"screen_img/howtoplay.png"), cv2.IMREAD_UNCHANGED)
    exit = cv2.imread(str(SCRIPT_DIR/"screen_img/exit.png"), cv2.IMREAD_UNCHANGED)

    #time-set
    num_of_secs = 500
    # num_of_secs = 100

    while True:
        frame = vs.read()
        frame = cv2.resize(frame, dsize=(2500, 1400))
        
        key = cv2.waitKey(1)
        if key == ord('1'): num = 1
        if key == ord('2'): num = 2
        if key == ord('3'): num = 3
        if key == ord('4'): num = 4
        if key == ord('5'): num = 5
        if key == ord('7'): num = 7
        if key == ord('8'): num = 8
        if cv2.waitKey(1) == ord('q'): exit()
        
        (corners, ids, rejected) = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)
         
        show_text(frame, gm.get_num(), ids, num_of_secs)

        n = gm.get_num()
        if gm.get_num() == 2:
            #timer
            m, s = divmod(num_of_secs, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            cv2.putText(frame, min_sec_format, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 8)
            num_of_secs = num_of_secs - 1
            if(num_of_secs == 0):
                gm.ending(ids)
        
        # detect ArUco markers in the input frame
        
        # verify *at least* one ArUco marker was detected
        if len(corners) > 0:
        # flatten the ArUco IDs list
            ids = ids.flatten()
            
            #*****************기능팀 추가******************
            gm.detect_ids(ids)
            
            # loop over the detected ArUCo corners
            for (markerCorner, markerID) in zip(corners, ids):
                # extract the marker corners (which are always returned
                # in top-left, top-right, bottom-right, and bottom-left
                # order)

                corners = markerCorner.reshape((4, 2))
                (topLeft, topRight, bottomRight, bottomLeft) = corners

                # convert each of the (x, y)-coordinate pairs to integers
                topRight = (int(topRight[0]), int(topRight[1]))
                bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
                bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
                topLeft = (int(topLeft[0]), int(topLeft[1]))
                
                if(distance(int(topRight[0]), int(topRight[1]), 1400, 1)) and gm.get_num() == 2:
                    SCRIPT_DIR = Path(__file__).parent
                    
                    if markerID == 50: explain = cv2.imread(str(SCRIPT_DIR/'explain_png/Bus.png'))
                    if markerID == 51: explain = cv2.imread('explain_png/Tree_planting.png')
                    if markerID == 52: explain = cv2.imread('explain_png/Recycle.png')
                    if markerID == 53: explain = cv2.imread('explain_png/unplug.png')
                    if markerID == 54: explain = cv2.imread('explain_png/recup.png')
                    if markerID == 55: explain = cv2.imread('explain_png/solar.png')
                    if markerID == 56: explain = cv2.imread('explain_png/wind.png')
                    if markerID == 57: explain = cv2.imread('explain_png/shopping_bag.png')
                    if markerID == 58: explain = cv2.imread('explain_png/light_off.png')
                    if markerID == 59: explain = cv2.imread('explain_png/bike.png')
                    
                    if markerID == 60: explain = cv2.imread('explain_png/factory.png')
                    if markerID == 61: explain = cv2.imread('explain_png/airC.png')
                    if markerID == 62: explain = cv2.imread('explain_png/meat.png')
                    if markerID == 63: explain = cv2.imread('explain_png/car.png')
                    if markerID == 64: explain = cv2.imread('explain_png/bag.png')
                    if markerID == 65: explain = cv2.imread('explain_png/foodwaste.png')
                    if markerID == 66: explain = cv2.imread('explain_png/waste.png')
                    if markerID == 67: explain = cv2.imread('explain_png/oil.png')
                    if markerID == 68: explain = cv2.imread('explain_png/pesticide.png')
                    if markerID == 69: explain = cv2.imread('explain_png/tree_cut.png')
                    
                    if explain is not None:
                        explain = cv2.resize(explain, dsize=(650, 300))
                        mask = explain[:, :, -1]
                        explain = explain[:, :, 0:3]
                        
                        rows, cols, channels = explain.shape #로고파일 픽셀값 저장
                        crop = frame[100:rows+100,100:cols+100]
                        #crop = frame[0:0,500:500]
                        cv2.copyTo(explain, mask, crop)

                # draw the bounding box of the ArUCo detection
                #cv2.line(frame, topLeft, topRight, (0, 255, 0), 2)
                #cv2.line(frame, topRight, bottomRight, (0, 255, 0), 2)
                #cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 2)
                #cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 2)
                
                # compute and draw the center (x, y)-coordinates of the
                # ArUco marker
                #cX = int((topLeft[0] + bottomRight[0]) / 2.0)
                #cY = int((topLeft[1] + bottomRight[1]) / 2.0)
                #cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)
                # draw the ArUco marker ID on the frameq
                if gm.get_num() == 1:
                    if markerID == 1: show_object(start, frame, topLeft)
                    if markerID == 2: show_help(help, frame, topLeft)
                    if markerID == 3: show_object(exit, frame, topLeft) 
                
                if gm.get_num() == 2:                
                    if markerID == 50: show_object(bus, frame, topLeft)
                    if markerID == 51: show_object(tree, frame, topLeft)
                    if markerID == 52: show_object(recycle, frame, topLeft)
                    if markerID == 53: show_object(unplug, frame, topLeft)
                    if markerID == 54: show_object(recup, frame, topLeft)
                    if markerID == 55: show_object(solar, frame, topLeft)
                    if markerID == 56: show_object(wind, frame, topLeft)
                    if markerID == 57: show_object(shopping_basket, frame, topLeft)
                    if markerID == 58: show_object(turn_off, frame, topLeft)
                    if markerID == 59: show_object(bike, frame, topLeft)
                    
                    if markerID == 60: show_object(factory, frame, topLeft)
                    if markerID == 61: show_object(airC, frame, topLeft)
                    if markerID == 62: show_object(meat, frame, topLeft)
                    if markerID == 63: show_object(car, frame, topLeft)
                    if markerID == 64: show_object(plastic_bag, frame, topLeft)
                    if markerID == 65: show_object(foodwaste, frame, topLeft)
                    if markerID == 66: show_object(waste, frame, topLeft)
                    if markerID == 67: show_object(oil, frame, topLeft)
                    if markerID == 68: show_object(pesticide, frame, topLeft)
                    if markerID == 69: show_object(tree_cut, frame, topLeft)    

                #cv2.putText(frame, str(markerID),
                #    (topLeft[0], topLeft[1] - 15),
                #    cv2.FONT_HERSHEY_SIMPLEX, 0.5, 
                #    (0, 255, 0), 2)
        
        # show the output frame
        cv2.imshow("Frame", frame)
        
        def information(frame):
            if(frame == 50):
                explanation = ("Trees absorb carbon dioxide. Carbon dioxide is the one of the main causes of climate change.")
            if(frame == 'factory'):
                explanation = ("The exhausts from factories accelerates air pollution.")
            if(frame == 'recycle'):
                explanation = ("We can transform waste plastic, fabric, etc into another goods to prevent resource abusing")
            if(frame == 'Unplug'):
                explanation = ("When electronic devices are plugged, they use stanby power even human is not actually using them. \nCurrently, most electricity is made of gas and oil emitting carbon")
            if(frame == 'reusableCup'):
                explanation = ("According to Canadian Evironment institute, using reusable cups helps in decreasing carbon emission if they are used over 220times than using disposable cups")
            if(frame == 'AirConditioner'):
                explanation = int("Air conditioner uses a lot of electricity\nCurrently, most electricity is made of gas and oil emitting carbon")
            if(frame == 'RenewableEnergy'):
                explanation = ("Renewable energy such as solar power and wind power decrease carbon emisison in making electricity")
            if(frame == 'Car'):
                explanation = ("Cars that move by gas and oil emits a lot of carbon dioxide. About 20% of carbon emission is from cars")
            if(frame == 'Bus'):
                explanation = ("Using public transportation's carbon emission amount is about 1/10 of driving cars")
            if(frame == 'Meat'):
                explanation = ("Growing cows and pigs for food emits more carbon than growing plants and fruits")
                
            print(explanation)
            return explanation
                
        # show the output frame
        cv2.imshow("Frame", frame)
    
# # do a bit of cleanup
# cv2.destroyAllWindows()
# vs.stop()

def show_object(image, frame, topLeft):
    image = cv2.resize(image, dsize=(180, 180))
    mask = image[:, :, -1]
    image = image[:, :, 0:3]
    
    #draw a image in video
    h, w = image.shape[:2]
    crop = frame[topLeft[1]:h+topLeft[1], topLeft[0]:w+topLeft[0]]
    cv2.copyTo(image, mask, crop)

def show_help(image, frame, topLeft):
    image = cv2.resize(image, dsize=(1000, 1000))
    mask = image[:, :, -1]
    image = image[:, :, 0:3]
    
    #draw a image in video
    h, w = image.shape[:2]
    crop = frame[topLeft[1]-500:h+topLeft[1]-500, topLeft[0]-500:w+topLeft[0]-500]
    cv2.copyTo(image, mask, crop)


def play_bgm():
    SCRIPT_DIR = Path(__file__).parent
    file = SCRIPT_DIR/'bgm/clearday.mp3'
    
    pygame.mixer.init()
    pygame.mixer.music.load(str(file))
    pygame.mixer.music.play()


def show_text(frame, number, ids, num_of_secs):
    if(number == 1):
        title = cv2.imread('screen_img/title.png')
        title = cv2.resize(title, dsize=(1500, 280))
        mask = title[:, :, -1]
        title = title[:, :, 0:3]
        
        rows, cols, channels = title.shape #로고파일 픽셀값 저장
        crop = frame[10:rows+10,500:cols+500]
        cv2.copyTo(title, mask, crop)
        
        title = cv2.imread('screen_img/title_help.png')
        title = cv2.resize(title, dsize=(1000, 100))
        mask = title[:, :, -1]
        title = title[:, :, 0:3]
        
        rows, cols, channels = title.shape #로고파일 픽셀값 저장
        crop = frame[260:rows+260,750:cols+750]
        cv2.copyTo(title, mask, crop)

    if(number == 2):
        image = cv2.imread('screen_img/earth_help.png')
        image = cv2.resize(image, dsize=(1500, 250))
        mask = image[:, :, -1]
        image = image[:, :, 0:3]
        
        rows, cols, channels = image.shape #로고파일 픽셀값 저장
        crop = frame[0:rows+0,500:cols+500]
        cv2.copyTo(image, mask, crop)
        

    if(number == 3):
        SCRIPT_DIR = Path(__file__).parent
        file = SCRIPT_DIR/'screen_img/good_ending.png'
        image = cv2.imread(str(file))
        image = cv2.resize(image, dsize=(2500, 1400))
        mask = image[:, :, -1]
        image = image[:, :, 0:3]
        
        rows, cols, channels = image.shape #로고파일 픽셀값 저장
        crop = frame[0:rows+0,0:cols+0]
        cv2.copyTo(image, mask, crop)
        
        cv2.putText(frame, str(gm.get_score()), (1100, 610), cv2.FONT_HERSHEY_PLAIN, 8, (255, 255, 255), 5)
        
    if(number == 4):
        SCRIPT_DIR = Path(__file__).parent
        file = SCRIPT_DIR/'screen_img/bad_ending.png'
        image = cv2.imread(str(file))
        image = cv2.resize(image, dsize=(2500, 1400))
        mask = image[:, :, -1]
        image = image[:, :, 0:3]
        
        rows, cols, channels = image.shape #로고파일 픽셀값 저장
        crop = frame[0:rows+0,0:cols+0]
        cv2.copyTo(image, mask, crop)

        cv2.putText(frame, str(gm.get_score()), (1100, 610), cv2.FONT_HERSHEY_PLAIN, 8, (255, 255, 255), 5)

    if(number == 5):
        SCRIPT_DIR = Path(__file__).parent
        file = SCRIPT_DIR/'screen_img/sobad_ending.png'
        image = cv2.imread(str(file))
        image = cv2.resize(image, dsize=(2500, 1400))
        mask = image[:, :, -1]
        image = image[:, :, 0:3]
        
        rows, cols, channels = image.shape #로고파일 픽셀값 저장
        crop = frame[0:rows+0,0:cols+0]
        cv2.copyTo(image, mask, crop)
        
        cv2.putText(frame, str(gm.get_score()), (1100, 610), cv2.FONT_HERSHEY_PLAIN, 8, (255, 255, 255), 5)
        
    if(number == 7):
        image = cv2.imread('screen_img/howtoplay.png')
        image = cv2.resize(image, dsize=(2500, 1400))
        mask = image[:, :, -1]
        image = image[:, :, 0:3]
        
        rows, cols, channels = image.shape #로고파일 픽셀값 저장
        crop = frame[0:rows+0,0:cols+0]
        cv2.copyTo(image, mask, crop)
