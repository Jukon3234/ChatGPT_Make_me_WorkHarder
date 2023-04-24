import os
import sys
import win32gui
import time
import cv2
import Function.Foundation
from PIL import Image


import pyautogui



class GBFPosition:

    def getItem():
        left, top, width, height = win32gui.GetWindowRect(Function.Foundation.WindowsHandle)
        image_path = 'target_image.png'
        scroll_distance = 50

        pyautogui.click(left, top)

        def locate_image():
            screenshot = Image.grab()
            location = pyautogui.locate(image_path, screenshot, region=(left, top, width, height))
            return location

        while True:
            location = locate_image()
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