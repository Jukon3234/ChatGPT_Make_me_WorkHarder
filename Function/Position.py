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
    

    def grayphoto(self):#先保留
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