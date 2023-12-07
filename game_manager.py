import pygame
from pathlib import Path
import sys
from play_video import play_video
import time

class GM:
    def __init__(self):
        self.score = 0
        self.num = 1

    #main 기능 제어
    def get_num(self):
        return self.num  

    #점수 리턴
    def get_score(self):
        return self.score

    #실시간 id 받아오기
    def detect_ids(self, ids):
        #게임 메인 화면
        if self.num == 1:
            self.main_scene(ids)

    #main_scene
    def main_scene(self, ids):
        OBJ_DICT = {
            "EARTH": 99,
            "START": 1,
            "HELP": 2,
            "EXIT": 3
        }
        #시작
        if OBJ_DICT["START"] in ids:
            self.game_start()
        #도움말
        # print(ids)
        # if OBJ_DICT["HELP"] in ids:
        #     self.num = 7
        #종료
        if OBJ_DICT["EXIT"] in ids:
            sys.exit()

    def game_start(self):
        play_video()
        self.play_bgm()
        self.num=2
        
    #Get ids for score
    def identify_id(self, ids):
        result = False
        good = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
        
        for id in ids:
            if id in good:
                #For notice --> Debug용
                self.set_score(10)
            else:
                self.set_score(-5)
    
    def set_score(self, score):
        self.score = self.score + score

    #Game Ending
    def ending(self, ids):
        #Compute Score
        for id in ids:
            self.identify_id(id)

        #엔딩 분기
        if self.score >= 50:    #good
            self.num = 3
        elif self.score >= 30:      #bad
            self.num = 4
        else:                   #so bad
            self.num = 5

        print(self.score)


    def play_bgm(self):
        SCRIPT_DIR = Path(__file__).parent
        file = SCRIPT_DIR/'bgm/clearday.mp3'

        pygame.mixer.init()
        pygame.mixer.music.load(str(file))
        pygame.mixer.music.play()

    #도움말 return
    def information(self, id):
        GOOD_DICT = {
            "Bus": 50,
            "Tree": 51,
            "Recycle": 52,
            "Unplug": 53,
            "ReusableCup": 54,
            "RenewableEnergy": 55,
            "Bicycle": 56,
            "ShoppingBasket": 57,
            "LightOff": 58,
            "Water": 59
        }
        BAD_DICT = {
            "TreeCut": 60,
            "SyntheticF": 61,
            "Oil": 62,
            "Meat": 63,
            "Waste": 64,
            "FoodWaste": 65,
            "Factory": 66,
            "PlasticBag": 67,
            "Car": 68,
            "AirConditioner": 69
        }

        explanation = ""
        if id == GOOD_DICT["Bus"]:
            explanation = "Using public transportation's carbon emission amount is about 1/10 of driving cars"
        if id == GOOD_DICT["Tree"]:
            explanation = "Trees absorb carbon dioxide. Carbon dioxide is the one of the main causes of climate change"
        if id == GOOD_DICT["Recycle"]:
            explanation = "We can transform waste plastic, fabric, etc into another goods to prevent resource abusing"
        if id == GOOD_DICT["Unplug"]:
            explanation = "When electronic devices are plugged, they use stanby power even the device is not actually used. \nCurrently, most electricity is made of gas and oil emitting carbon"
        if id == GOOD_DICT["ReusableCup"]:
            explanation = "According to Canadian Evironment institute, using reusable cups helps in decreasing carbon emission if they are used over 220times than using disposable cups"
        if id == GOOD_DICT["RenewableEnergy"]:
            explanation = "Renewable energy such as solar power and wind power decrease carbon emisison in making electricity"
        if id == GOOD_DICT["Bicycle"]:
            explanation = "Riding bicycle instead of car decreases carbon emission"
        if id == GOOD_DICT["ShoppingBasket"]:
            explanation = "Using reusable shopping basket decrease amount used disposable bag"
        if id == GOOD_DICT["LightOff"]:
            explanation = "Currently, most electricity is made of gas and oil emitting carbon"
        if id == GOOD_DICT["Water"]:
            explanation = "Reducing water waste helps to decrease water pollution"
        if id == BAD_DICT["Treecut"]:
            explanation = "Trees absorb carbon dioxide. Carbon dioxide is the one of the main causes of climate change"
        if id == BAD_DICT["SyntheticF"]:
            explanation = "Synthetic fertilizer pollutes earth and water"
        if id == BAD_DICT["Oil"]:
            explanation = "Oil is the main energy resource and it emits a lot of carbon when it burns"
        if id == BAD_DICT["Meat"]:
            explanation = "Growing cows and pigs for food emits more carbon than growing plants and fruits"
        if id == BAD_DICT["Waste"]:
            explanation = "When wastes are landfilled or incinerated, earth and air are polluted"
        if id == BAD_DICT["FoodWaste"]:
            explanation = "When food wastes are landfilled or incinerated, earth and air are polluted"
        if id == BAD_DICT["factory"]:
            explanation = "The exhausts from factories accelerates air pollution."
        if id == BAD_DICT["PlasticBag"]:
            explanation = "Plastic bag takes many years to for them to decompose. In addition, toxic substances are released into the soil"
        if id == BAD_DICT["Car"]:
            explanation = "Cars that move by gas and oil emits a lot of carbon dioxide. About 20% of carbon emission is from cars"
        if id == BAD_DICT["AirConditioner"]:
            explanation = "Air conditioner uses a lot of electricity\nCurrently, most electricity is made of gas and oil emitting carbon"

        print(explanation)
        return explanation



        