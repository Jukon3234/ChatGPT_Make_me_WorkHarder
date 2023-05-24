from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Function.Picture import GetPicFunction
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

    def SysGetPic(self):#抓小圖
        window_rect = win32gui.GetWindowRect(Fun.WindowsHandle)
        x, y, width, height = window_rect
        print("Fun.WindowsHandle: ",Fun.WindowsHandle)
        screen = QApplication.primaryScreen()
        Cutcapture = screen.grabWindow(Fun.WindowsHandle, 92, 380, 300, 150)
        Cutcapture.save("./systemdata/img/systemimg/CUTPIC.png")
    
    def DC_Get_Verify(self):        
        if Fun.DCBOT_Token == None:
            print("未設定token")
            return
        else:
            x = GetPicFunction()
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
                    await channel.send("偵測到系統驗證，需解鎖")
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
                Picture = cv2.imread('./systemdata/img/systemimg/BLOCK.PNG')
    
                if x.PicDetTF(Picture) == False:
                    await message.channel.send('解鎖成功')
                    x.GoHome()
                    await client.close()
                elif x.PicDetTF(Picture) == True:
                    channel = client.get_channel(int(Fun.DCBOT_ChannalID))
                    await message.channel.send('解鎖失敗 畫面重整')
                    self.SysGetPic()
                    await channel.send(file = discord.File('./systemdata/img/systemimg/CUTPIC.png'))
                    await message.channel.send('請再輸入一次:')
            client.run(token)

    def FuncForunlock(self, systemUnlock):
        x = GetPicFunction()
        mouse_pos = QCursor.pos()
        Picture = cv2.imread('./systemdata/img/systemimg/InsertForm.PNG')
        lox,loy = x.PicDet(Picture)
        text = str(systemUnlock)
        pyperclip.copy(text)
        pyautogui.click(lox+50,loy+55)        
        pyautogui.hotkey('ctrl', 'v')
        Picture = cv2.imread('./systemdata/img/systemimg/Send.PNG')
        lox,loy = x.PicDet(Picture)
        pyautogui.click(lox+50,loy+55)
        QCursor.setPos(mouse_pos)


            