from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2
import numpy as np
import discord
import asyncio
import win32gui
import Function.Foundation as Fun
import pyautogui
import time
import pyperclip

class GetBlockDET:
    def FuncBlockPicDet(self):#檢測是否有阻擋圖
        window_rect = win32gui.GetWindowRect(Fun.WindowsHandle)
        x, y, width, height = window_rect
        print("Fun.WindowsHandle: ",Fun.WindowsHandle)
        screen = QApplication.primaryScreen()
        Fun.capture = screen.grabWindow(Fun.WindowsHandle)
        Fun.capture.save("./systemdata/img/systemimg/screenshot.png")
        PicCapture = cv2.imread("./systemdata/img/systemimg/screenshot.png")
        template = cv2.imread('./systemdata/img/systemimg/BLOCK.PNG')

        result = cv2.matchTemplate(PicCapture, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.9
        Fun.locations = np.where(result >= threshold)
        print("locations:", Fun.locations)

        if any(Fun.locations[0]):
            return True
        else: 
            return False

    def SysGetPic(self):#抓小圖
        window_rect = win32gui.GetWindowRect(Fun.WindowsHandle)
        x, y, width, height = window_rect
        print("Fun.WindowsHandle: ",Fun.WindowsHandle)
        screen = QApplication.primaryScreen()
        Fun.capture = screen.grabWindow(Fun.WindowsHandle)
        Fun.capture.save("./systemdata/img/systemimg/screenshot.png")
        PicCapture = cv2.imread("./systemdata/img/systemimg/screenshot.png")
        template = cv2.imread('./systemdata/img/systemimg/BLOCK.PNG')        

        match_locations = []
        for pt in zip(*Fun.locations[::-1]):
            match_locations.append((pt[0] + x, pt[1] + y))

        if any(Fun.locations[0]):
            Fun.BlockLocation = match_locations[0]
            print("match_locations:", match_locations[0])
            Cutcapture = screen.grabWindow(Fun.WindowsHandle, 92, 380, 300, 150)
            Cutcapture.save("./systemdata/img/systemimg/CUTPIC.png")
    
    def DC_Get_Verify(self):
        if Fun.DCBOT_Token == None:
            print("未設定token")
            return
        else:
            print("Token:", Fun.DCBOT_Token)
            print("Channel_ID:", Fun.DCBOT_ChannalID)
            token = Fun.DCBOT_Token
            intents = discord.Intents.all()
            intents.message_content = True
            client = discord.Client(intents = intents)

            @client.event
            async def on_ready():
                print('目前登入身份：', client.user)
                channel = client.get_channel(int(Fun.DCBOT_ChannalID))
                try:
                    await channel.send("偵測到阻饒，需解鎖")
                    await channel.send(file = discord.File('./systemdata/img/systemimg/CUTPIC.png'))
                    await channel.send("請輸入驗證碼:")
                except:
                    print("出問題了請檢查")
                    await client.close()

            @client.event
            async def on_message(message):
                if message.author == client.user:
                    return
                
    
                systemUnlock = message.content
                print("message: ",systemUnlock)
                self.FuncForunlock(systemUnlock)
                time.sleep(3)
    
                if self.FuncBlockPicDet() == False:
                    await message.channel.send('解鎖成功')
                    Picture = cv2.imread('./systemdata/img/systemimg/home.PNG')
                    lox,loy = self.PicDet(Picture)
                    click_pos = QPoint(lox+50,loy+55)
                    await client.close()
                elif self.FuncBlockPicDet() == True:
                    channel = client.get_channel(int(Fun.DCBOT_ChannalID))
                    await message.channel.send('解鎖失敗 畫面重整')
                    self.SysGetPic()
                    await channel.send(file = discord.File('./systemdata/img/systemimg/CUTPIC.png'))
                    await message.channel.send('請再輸入一次:')
            client.run(token)
            
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

    def getkeyboard_LAY(self):
        user32 = ctypes.WinDLL('user32', use_last_error=True)
        curr_window = user32.GetForegroundWindow()
        thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
        klid = user32.GetKeyboardLayout(thread_id)
        lid = klid & (2**16 - 1)
        lid_hex = hex(lid)
        return lid_hex

    def FuncForunlock(self, systemUnlock):
        mouse_pos = QCursor.pos()
        Picture = cv2.imread('./systemdata/img/systemimg/InsertForm.PNG')
        lox,loy = self.PicDet(Picture)
        text = str(systemUnlock)
        pyperclip.copy(text)
        pyautogui.click(lox+50,loy+55)        
        pyautogui.hotkey('ctrl', 'v')
        Picture = cv2.imread('./systemdata/img/systemimg/Send.PNG')
        lox,loy = self.PicDet(Picture)
        pyautogui.click(lox+50,loy+55)
        QCursor.setPos(mouse_pos)


            