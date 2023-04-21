from threading import Thread
import os
import sys
import win32gui
import time
import cv2
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import Function.Foundation
import numpy as np
from PIL import Image


class GBFPosition:
    def postion(self):
        screen= QApplication.primaryScreen()
        windowsimage = screen.grabWindow(Function.Foundation.WindowsHandle).toImage()
        windowsimage = windowsimage.convertToFormat(4)        
        width = windowsimage.width()
        height = windowsimage.height()
        ptr = windowsimage.bits()
        ptr.setsize(windowsimage.byteCount())
        arr = np.array(ptr).reshape(height,width,4)
        im = Image.fromarray(arr) #組合
        GrayImage = cv2.cvtColor(np.asarray(im),cv2.COLOR_BGR2GRAY)
        cv2.imwrite("./systemdata/img/printscreen/testscreen.png",GrayImage)
        print("save success")
    

    def MakeGrayPhoto(self):#先保留
        screen= QApplication.primaryScreen()
        windowsimage = screen.grabWindow(Function.Foundation.WindowsHandle).toImage()
        windowsimage = windowsimage.convertToFormat(4)
        
        width = windowsimage.width()
        height = windowsimage.height()
        ptr = windowsimage.bits()
        ptr.setsize(windowsimage.byteCount())
        arr = np.array(ptr).reshape(height,width,4)
        im = Image.fromarray(arr) #組合
        GrayImage = cv2.cvtColor(np.asarray(im),cv2.COLOR_BGR2GRAY)
        cv2.imwrite("./systemdata/img/printscreen/testscreen.png",GrayImage)
        print("save success")

#http://13.231.129.69/2020/08/13/python-%E8%87%AA%E5%8B%95%E5%8C%96%E5%B7%A5%E5%85%B7-pyautogui-%E9%87%8B%E6%94%BE%E4%BD%A0%E7%9A%84%E9%9B%99%E6%89%8B/
#https://blog.csdn.net/qq_42069296/article/details/121853190