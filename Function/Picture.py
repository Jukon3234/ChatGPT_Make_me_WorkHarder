from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
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
    
    
class GetPicFunction:
    
    def PicDet(self,Picture):#檢測圖位置
        window_rect = win32gui.GetWindowRect(Fun.WindowsHandle)
        x, y, width, height = window_rect
        screen = QApplication.primaryScreen()
        Fun.capture = screen.grabWindow(Fun.WindowsHandle)
        Fun.capture.save("./systemdata/img/systemimg/screenshot.png")
        PicCapture = cv2.imread("./systemdata/img/systemimg/screenshot.png")

        result = cv2.matchTemplate(PicCapture, Picture, cv2.TM_CCOEFF_NORMED)
        threshold = 0.9
        locations = np.where(result >= threshold)
        Xmatch_locations = []
        Ymatch_locations = []
        for pt in zip(*locations[::-1]):
            Xmatch_locations.append(pt[0] + x)
            Ymatch_locations.append(pt[1] + y)
        if any(locations[0]):
            return Xmatch_locations[0],Ymatch_locations[0]            
        else: 
            return None,None
    
    def ClickPIC(self,Picture):
        while not Fun.StopFunction:
            lox,loy = self.PicDet(Picture)
            if lox == None:
                pyautogui.scroll(-200)
            else:                                
                pyautogui.click(lox+50,loy+55)
                break
                time.sleep(0.5)
    
    def LoopWait(self,Picture):
        #連續偵測是否已經轉到畫面            
        while True:
            if self.PicDetTF(Picture) == True:
                break
            else:
                time.sleep(0.5)  # 等待0.5秒后再次检测


    def PicDetTF(self,Picture):#檢測圖是否存在
        window_rect = win32gui.GetWindowRect(Fun.WindowsHandle)
        x, y, width, height = window_rect
        print("Fun.WindowsHandle: ",Fun.WindowsHandle)
        screen = QApplication.primaryScreen()
        Fun.capture = screen.grabWindow(Fun.WindowsHandle)
        Fun.capture.save("./systemdata/img/systemimg/screenshot.png")
        PicCapture = cv2.imread("./systemdata/img/systemimg/screenshot.png")
        result = cv2.matchTemplate(PicCapture, Picture, cv2.TM_CCOEFF_NORMED)
        threshold = 0.9
        locations = np.where(result >= threshold)
        if any(locations[0]):
            return True            
        else: 
            return False
        
    def GoHome(self):
        Picture=cv2.imread("./systemdata/img/systemimg/home.PNG")
        lox,loy = self.PicDet(Picture)
        pyautogui.click(lox+50,loy+55)

    def HomepageCheck(self):
        #確認進場前為主畫面
        Picture = cv2.imread("./systemdata/img/systemimg/Top.PNG")
        if self.PicDetTF(Picture) == False:
            self.GoHome()
            #連續偵測是否已經轉到畫面            
            while True:
                if self.PicDetTF(Picture) == True:
                    break
                else:
                    time.sleep(0.5)  # 等待0.5秒后再次检测