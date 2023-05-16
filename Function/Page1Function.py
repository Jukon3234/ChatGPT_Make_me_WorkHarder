
from threading import Thread
from Function.DiscordBlockDet import GetBlockDET
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


#轉世頁面內容
#1.需要向下尋找轉世的item
#2.要找到指定的關卡item
#3.進入關卡後分成3頁面 左中右 透過左右按鈕切畫面
#4.怪物以轉世關卡分類
#5.隊伍可以指定X/Y方法，或是額外不選擇，僅使用前一場使用的隊伍
#6.需要FA直到關卡完成。若中途失敗可選擇是否使用大紅復活，復活後執行reload auto

class RunFunction:
    #===================================debug
    def debugLog(self):
        print("StopFunction: ", Fun.StopFunction)
        print("Function1FightCount: ", Fun.Function1FightCount)
        print("TypeSelect: ", Fun.TypeSelect)
        print("RunFlag: ", Fun.RunFlag)    
    #====================================function
    def RunFGscrept(self):
        if Fun.RunFlag == False:
            Fun.RunFlag = True
            Fun.StopFunction = False
            if Fun.Function1FightCount == 0:
                #無限迴圈
                def GBFloop():
                    while Fun.StopFunction == False:
                        try:
                            print(f"test run run run: 無上限") 
                            time.sleep(1)
                            print("stopfuntion=",Fun.StopFunction)
                            print("Function1FightCount=",Fun.Function1FightCount)
                            Fun.RunFlag = False
                        except:
                            print("Function fail")
                            Fun.RunFlag = False
            else:
                #有限迴圈
                def GBFloop():
                    for i in range(Fun.Function1FightCount):
                        try:
                            C=i+1
                            TC=Fun.Function1FightCount                            
                            print(f"test run run run: {C}/{TC}")
                            Picture=cv2.imread("./systemdata/img/systemimg/Arcarum.PNG")
                            Flag = True
                            while(Flag):
                                lox,loy = self.PicDet(Picture)
                                if any(lox):
                                    pyautogui.click(lox+50,loy+55)
                                    Flag=False
                                    time.sleep(0.5)
                                else:
                                    pyautogui.scroll(-12)
                            self.GoHome()

                            time.sleep(1)

                            print("stopfunction=",Fun.StopFunction)
                            print("Function1FightCount=",Fun.Function1FightCount)
                            if Fun.StopFunction:
                                break
                        except:
                            print("Function fail")
                            Fun.RunFlag = False
                    Fun.RunFlag = False
        
            global functionthread
            functionthread = Thread(target=GBFloop)
            functionthread.setDaemon(True)
            functionthread.start()
    def GoHome(self):
        Picture=cv2.imread("./systemdata/img/systemimg/home.PNG")
        lox,loy = self.PicDet(Picture)
        pyautogui.click(lox+50,loy+55)
    
    def PicDet(self,Picture):#檢測圖位置
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
        Xmatch_locations = []
        Ymatch_locations = []
        for pt in zip(*locations[::-1]):
            Xmatch_locations.append(pt[0] + x)
            Ymatch_locations.append(pt[1] + y)
        print("PIClocations:", Xmatch_locations[0],Ymatch_locations[0])
        return Xmatch_locations[0],Ymatch_locations[0]
        
    def ReadMap(self):
        if Fun.Map == "1":
            if Fun.challenge == "1":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "2":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "3":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "4":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "5":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "6":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "7":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "8":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "9":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "10":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
        elif Fun.Map == "2":
            if Fun.challenge == "1":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "2":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "3":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "4":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "5":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "6":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "7":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "8":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "9":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "10":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
        elif Fun.Map == "3":
            if Fun.challenge == "1":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "2":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "3":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "4":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "5":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "6":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "7":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "8":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "9":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "10":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
        elif Fun.Map == "4":
            if Fun.challenge == "1":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "2":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "3":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "4":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "5":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "6":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "7":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "8":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "9":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "10":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
        elif Fun.Map == "5":
            if Fun.challenge == "1":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "2":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "3":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "4":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "5":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "6":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "7":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
        elif Fun.Map == "6":
            if Fun.challenge == "1":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "2":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "3":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "4":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "5":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "6":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "7":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
        elif Fun.Map == "7":
            if Fun.challenge == "1":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "2":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "3":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "4":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "5":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "6":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "7":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
        elif Fun.Map == "8":
            if Fun.challenge == "1":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "2":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "3":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "4":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "5":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "6":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "7":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
        elif Fun.Map == "9":
            if Fun.challenge == "1":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "2":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "3":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "4":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "5":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "6":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "7":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "8":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "9":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "10":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "11":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "12":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "13":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "14":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
        else:
            print("Error")