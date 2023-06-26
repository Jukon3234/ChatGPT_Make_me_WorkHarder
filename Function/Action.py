from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Function.Picture import GetPicFunction
import cv2
import os
import sys
import time
import Function.Foundation as Fun
import pyautogui
import time
import pyperclip
import win32gui
import numpy as np
import cv2
import random
import json

class FCAction:
    def GoHome(self):
        x = GetPicFunction()
        Picture=cv2.imread("./systemdata/img/systemimg/home.PNG")
        PsizeH,PsizeW = x.PicSize(Picture)
        lox,loy = x.PicDet(Picture)
        CurX = lox+(PsizeW/2)
        CurY = loy+(PsizeH/2)
        self.curmvClick(CurX,CurY)
    
    def Reload(self):
        x = GetPicFunction()
        Picture=cv2.imread("./systemdata/img/systemimg/Reload.PNG")
        PsizeH,PsizeW = x.PicSize(Picture)
        lox,loy = x.PicDet(Picture)
        CurX = lox+(PsizeW/2)
        CurY = loy+(PsizeH/2)
        self.curmvClick(CurX,CurY)
    
    def HomepageCheck(self): #Homepage處理
        x = GetPicFunction()
        Picture = cv2.imread("./systemdata/img/systemimg/Top.PNG")
        if x.PicDetTF(Picture) == False:
            print("Homepage check = false")
            self.GoHome()
            #連續偵測是否已經轉到畫面
            while True:
                if x.PicDetTF(Picture) == True:
                    break
                else:
                    time.sleep(0.5)  # 等待0.5秒后再次檢測

    def MoveCurtoGamePage(self):
        window_rect = win32gui.GetWindowRect(Fun.WindowsHandle)
        lox,loy,Loxx,Loyy = window_rect
        print(lox,loy,Loxx,Loyy)
        self.curmv(lox+((Loxx-lox)/2),loy+((Loyy-loy)/2))

    def ClickPIC(self,Picture):
        x = GetPicFunction()
        PsizeH,PsizeW = x.PicSize(Picture)
        while not Fun.StopFunction:
            lox,loy = x.PicDet(Picture)
            if lox == None:
                pyautogui.scroll(-200)
            else:
                CurX = lox+(PsizeW/2)
                CurY = loy+(PsizeH/2)
                self.curmvClick(CurX,CurY)
                break
                time.sleep(0.5)
    
    def OnePic_LoopWait(self,Target):
        x = GetPicFunction()
        #連續偵測是否已經轉到畫面            
        while True:
            if x.PicDetTF(Target) == True:
                break
            else:
                time.sleep(0.5)  # 等待0.5秒后再次檢測
    
    def TwoPIC_LoopWait(self,Target,Non_Target):#當看到不同的item 可以回傳設定做切換判斷
        x = GetPicFunction()
        #連續偵測是否已經轉到畫面            
        while True:
            if x.PicDetTF(Target) == True :
                return True
                break
            elif x.PicDetTF(Non_Target) == True :
                return False
                break
            else:
                time.sleep(0.5)  # 等待0.5秒后再次檢測
    
    def curmvClick(self,x,y): #位移後點擊
        random_Curmove = random.randint(Fun.NCurmoveTimeRan,Fun.CurmoveTimeRan)
        CurTime=(Fun.CurmoveTime/1000)+ random_Curmove/1000
        print("CurTime",CurTime)
        pyautogui.moveTo(x, y, duration = CurTime)
        pyautogui.mouseDown(x, y, button = 'left')
        pyautogui.mouseUp(x, y, button = 'left')

    def curmv(self,x,y): #僅位移
        random_Curmove = random.randint(Fun.NCurmoveTimeRan,Fun.CurmoveTimeRan)
        CurTime=(Fun.CurmoveTime/1000)+ random_Curmove/1000
        print("CurTime",CurTime)
        pyautogui.moveTo(x, y, duration = CurTime)
    
    def LoadFile(self):
        if os.path.exists('./systemdata/datasave/data.json'):
            SaveFile = open('systemdata/datasave/data.json')
        else:
            SaveFile = open('systemdata/datasave/Default.json')
        savedata= json.load(SaveFile)

        Fun.Function1FightCount = savedata['function']['FightCount']        
        Fun.DCBOT_Token = savedata['Bot']['TOKEN']
        Fun.DCBOT_ChannalID = savedata['Bot']['Channal_ID']
        Fun.DCBOT_EN = savedata['Bot']['Enabled']
        Fun.StepDelay = savedata['Delay']['StepDelay']
        Fun.stepdelayRandom = savedata['Delay']['stepdelayRandom']
        Fun.RoundDelay = savedata['Delay']['RoundDelay']
        Fun.RounddelayRandom = savedata['Delay']['RounddelayRandom']
        Fun.CurmoveTime = savedata['Delay']['CurMoveTime']
        Fun.CurmoveTimeRandom = savedata['Delay']['CurmoveTimeRan']
        Fun.RandomX = savedata['Point']['RandomXSpin']
        Fun.RandomY = savedata['Point']['RandomYSpin']        
    
    def SaveChange(Self):
        Savedata = {}
        Savedata['function'] = {'FightCount': Fun.Function1FightCount, 'TypeSelect': 0}
        Savedata['Bot'] = {'TOKEN': Fun.DCBOT_Token,'Channal_ID': Fun.DCBOT_ChannalID,'Enabled' : Fun.DCBOT_EN}
        Savedata['Delay'] = {'StepDelay': Fun.StepDelay, 'RoundDelay': Fun.RoundDelay,'stepdelayRandom': Fun.stepdelayRandom,'RounddelayRandom': Fun.RounddelayRandom,'CurMoveTime': Fun.CurmoveTime,'CurmoveTimeRan': Fun.CurmoveTimeRandom}
        Savedata['Point'] = {'RandomXSpin' : Fun.RandomX,'RandomYSpin' : Fun.RandomY}
        with open('systemdata/datasave/data.json', 'w') as datafile:
            json.dump(Savedata,datafile)
    
