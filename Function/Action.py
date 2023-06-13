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

class FCAction:

    x = GetPicFunction()

    def GoHome(self):
        x = GetPicFunction()
        Picture=cv2.imread("./systemdata/img/systemimg/home.PNG")
        lox,loy = x.PicDet(Picture)
        pyautogui.click(lox+50,loy+55)

    def Reload(self):
        x = GetPicFunction()
        Picture=cv2.imread("./systemdata/img/systemimg/Reload.PNG")
        lox,loy = x.PicDet(Picture)
        pyautogui.click(lox+50,loy+55)
    
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
        pyautogui.moveTo(lox+((Loxx-lox)/2),loy+((Loyy-loy)/2))

    def ClickPIC(self,Picture):
        x = GetPicFunction()
        while not Fun.StopFunction:
            lox,loy = x.PicDet(Picture)
            if lox == None:
                pyautogui.scroll(-200)
            else:                                
                pyautogui.click(lox+50,loy+55)
                break
                time.sleep(0.5)
    
    def LoopWait(self,Picture):
        x = GetPicFunction()
        #連續偵測是否已經轉到畫面            
        while True:
            if x.PicDetTF(Picture) == True:
                break
            else:
                time.sleep(0.5)  # 等待0.5秒后再次檢測