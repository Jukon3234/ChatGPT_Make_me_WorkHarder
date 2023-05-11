import Function.Foundation as Fun
import cv2
import numpy as np
import discord
import asyncio

class GetBlockDET:
    def FuncBlockPicDet(self):#檢測是否有阻擋圖
        window_rect = win32gui.GetWindowRect(Fun.WindowsHandle)
        x, y, width, height = window_rect
        print("Fun.WindowsHandle: ",Fun.WindowsHandle)
        screen = QApplication.primaryScreen()
        Fun.capture = screen.grabWindow(Fun.WindowsHandle)
        Fun.capture.save("./systemdata/img/screenshot.png")
        PicCapture = cv2.imread("./systemdata/img/screenshot.png")
        template = cv2.imread('./systemdata/img/BLOCK.PNG')

        result = cv2.matchTemplate(PicCapture, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.9
        locations = np.where(result >= threshold)
        print("locations:", locations)

        if any(locations[0]):
            return True
        else: 
            return False

    def SysGetPic(self):#抓小圖
        window_rect = win32gui.GetWindowRect(Fun.WindowsHandle)
        x, y, width, height = window_rect
        print("Fun.WindowsHandle: ",Fun.WindowsHandle)
        screen = QApplication.primaryScreen()
        Fun.capture = screen.grabWindow(Fun.WindowsHandle)
        Fun.capture.save("./systemdata/img/screenshot.png")
        PicCapture = cv2.imread("./systemdata/img/screenshot.png")
        template = cv2.imread('./systemdata/img/BLOCK.PNG')        

        match_locations = []
        for pt in zip(*locations[::-1]):
            match_locations.append((pt[0] + x, pt[1] + y))

        if any(locations[0]):
            Fun.BlockLocation = match_locations[0]
            print("match_locations:", match_locations[0])
            Cutcapture = screen.grabWindow(Fun.WindowsHandle, 92, 380, 300, 150)
            Cutcapture.save("./systemdata/img/CUTPIC.png")
    
    def DC_Get_Verify(self):
        if Fun.DCBOT_Token == None:
            print("未設定token")
            return
        else:    
            token = Fun.DCBOT_Token
            intents = discord.Intents.all()
            intents.message_content = True
            client = discord.Client(intents = intents)
            channel_id = Fun.DCBOT_ChannalID  # 替换为目标频道的 ID
            channel = client.get_channel(channel_id)
            @client.event
            async def on_ready():
                print('目前登入身份：', client.user)
                try:                
                    await channel.send("偵測到阻饒，需解鎖")
                    await channel.send(file = discord.File('./systemdata/img/CUTPIC.png'))
                    await channel.send("請輸入驗證碼:")
                    print("Block:",Fun.BlockFlag)
                except:
                    print("出問題了請檢查")
                    await client.close()

    
            @client.event
            async def on_message(message):
                if message.author == client.user:
                    return
    
                Fun.systemUnlock = message.content
                print("message: ",Fun.systemUnlock)
                #self.FuncForunlock()
    
                if self.FuncBlockPicDet() == False:
                    await message.channel.send('解鎖成功')
                    await client.close()
                elif self.FuncBlockPicDet() == True:
                    await message.channel.send('解鎖失敗 畫面重整')
                    self.SysGetPic()
                    await channel.send(file = discord.File('./systemdata/img/CUTPIC.png'))
                    await message.channel.send('請再輸入一次:')
            client.run(token)