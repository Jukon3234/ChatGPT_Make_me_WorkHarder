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