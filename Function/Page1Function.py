
from threading import Thread
from Function.DiscordBlockDet import GetBlockDET
from Function.Picture import GetPicFunction
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
            x = GetPicFunction()
            x.HomepageCheck()
            #找到主畫面時
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
                        C=i+1
                        TC=Fun.Function1FightCount                            
                        print(f"test run run run: {C}/{TC}")                        
                                
                        #找到轉世                        
                        Picture = cv2.imread("./systemdata/img/systemimg/Arcarum.PNG")                                                
                        x.ClickPIC(Picture)
                        #等畫面看到title
                        Picture = cv2.imread("./systemdata/img/systemimg/Title.PNG")
                        x.LoopWait(Picture)
                        #找到關卡
                        Picture = Fun.ReadArcarumPIC
                        x.ClickPIC(Picture)
                        
                        #self.GoHome()
                        time.sleep(1)
                        print("stopfunction=",Fun.StopFunction)
                        print("Function1FightCount=",Fun.Function1FightCount)
                        if Fun.StopFunction:
                            break
                    Fun.RunFlag = False
        
            global functionthread
            functionthread = Thread(target=GBFloop)
            functionthread.setDaemon(True)
            functionthread.start()