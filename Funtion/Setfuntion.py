
from threading import Thread
import os
import sys
import time


RunFlag = False
StopFuntion = False
FightCount = "0"
IntFightCount = 0
RunFlag = False
TypeSelect = 0

def ScreptRunFlag():
    global RunFlag
    RunFlag = True
    print("RunFlag：",RunFlag)

#===================================系統動作
def Stop():
    global StopFuntion
    StopFuntion = True

def reset():
    global StopFuntion
    StopFuntion = False
    
def ScreptRunFlag():
    global RunFlag
    RunFlag = True
    print("RunFlag：",RunFlag)

def ScreptStopFlag():
    global RunFlag
    RunFlag = False
    print("RunFlag：",RunFlag)
    
def OptionHelp():
    messagebox.showinfo('Help','Copy right BruceJH')

#===================================資料存儲
    
def countset():
    global FightCount    
    
    if CountEntry.get()== "" or CountEntry.get()== "0":
        FightCount = 0
        print("FightCount：",FightCount)
    else:
        FightCount = CountEntry.get()
        print("FightCount：",FightCount)
        fcset=("Set!! ")
    msg=tk.Message(debugger,text=fcset,font=("Algerian",12,"bold"),padx=1,pady=1,width=100)
    msg.grid(row=0,column=4)
    
def typeset(event):  
    global TypeSelect  
    TypeSelect = SelectBox.current()
    print("TypeSelect= ",TypeSelect)    
#===================================資料存儲


#===================================debug
def debugLog():
    print("StopFuntion: ", StopFuntion)
    print("FightCount: ", FightCount)
    print("IntFightCount: ", IntFightCount)
    print("TypeSelect: ", TypeSelect)
    print("RunFlag: ", RunFlag)


#====================================function
def RunFGscrept():
    if RunFlag==False:
        ScreptRunFlag()
        reset()
        IntFightCount = int(FightCount)
        if IntFightCount == 0:
            #無限迴圈
            def GBFloop():
                while StopFuntion == False:              
                    print(f"test run run run: 無上限") 
                    time.sleep(1)
                    print("stopfuntion=",StopFuntion)
                    print("FightCount=",IntFightCount)
                ScreptStopFlag()
        else:
            #有限迴圈
            def GBFloop():
                for i in range(IntFightCount):
                    C=i+1
                    TC=IntFightCount                
                    print(f"test run run run: {C}/{TC}")  
                    time.sleep(1)
                    print("stopfuntion=",StopFuntion)
                    print("FightCount=",IntFightCount)  
                    if StopFuntion:
                        print('函数停止运行')
                        ScreptRunFlag()
                        break
                ScreptStopFlag()
        global funtionthread
        funtionthread = Thread(target=GBFloop)
        funtionthread.setDaemon(True)
        funtionthread.start()
        
    
    