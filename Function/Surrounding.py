import os
import sys
import win32gui
import time
import cv2
import Function.Foundation
from PIL import Image
import pyautogui

#環境設定用
#按下這個function有可能會造成與原本玩家設定不符，需額外警告玩家
#環境設定需求:
#1.將遊戲頁面整理成頁面大小2
#2.使用半水及半粉需設定為無通知視窗
#3.設定為FA
#4.設定進關前可點擊FA

class GBFSettingSurronding:

    def SettingItem():
        left, top, width, height = win32gui.GetWindowRect(Function.Foundation.WindowsHandle)
        image_paths = ['target_image1.png', 'target_image2.png', 'target_image3.png']
        scroll_distance = 50

        pyautogui.click(left, top)

        def locate_image(image_path):
            screenshot = Image.grab()
            location = pyautogui.locate(image_path, screenshot, region=(left, top, width, height))
            return location

        location=locate_image(image_paths[0])
        if location is not None:
            click_x, click_y = pyautogui.center(location)
            pyautogui.click(click_x, click_y)
        else:
            print("找不到menu")
        
        location=locate_image(image_paths[1])
        if location is not None:
            click_x, click_y = pyautogui.center(location)
            pyautogui.click(click_x, click_y)
        else:
            print("找不到半水設定")
        
        location=locate_image(image_paths[2])
        if location is not None:
            click_x, click_y = pyautogui.center(location)
            pyautogui.click(click_x, click_y)
        else:
            print("找不到半粉設定")
        


        while True:
            location = locate_image(image_path)
            if location is not None:
                break
            pyautogui.scroll(scroll_distance)
            time.sleep(0.5)
            if pyautogui.position()[1] >= top + height - scroll_distance:
                print("沒有這個物件")
                break

        if location is not None:
            click_x, click_y = pyautogui.center(location)
            pyautogui.click(click_x, click_y)