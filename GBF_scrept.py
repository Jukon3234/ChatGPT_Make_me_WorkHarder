from ctypes import windll, byref
from ctypes.wintypes import HWND, POINT
import time
import sys
import win32gui
import os
import pyautogui as pag
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from threading import Thread
from PIL import Image, ImageTk



PostMessageW = windll.user32.PostMessageW
ClientToScreen = windll.user32.ClientToScreen

    #鎖定視窗框架
    #鎖定視窗框架
        #選擇執行方案
        #刷方陣
            #方陣屬性
            #方陣ver
            #次數
        #刷方陣
        
        #刷轉世
        #刷轉世
        
        #刷活動
        #刷活動
    #選擇執行方案
    
    #執行框架
        #刷方陣
        #刷方陣
        
        #刷轉世
        #刷轉世
        
        #刷活動
        #刷活動    
    
    #執行框架

WM_MOUSEMOVE = 0x0200
WM_LBUTTONDOWN = 0x0201
WM_LBUTTONUP = 0x202
WM_MOUSEWHEEL = 0x020A
WHEEL_DELTA = 120

#===================================APPinit
StopFuntion = False
FightCount = "0"
IntFightCount = 0
fcset=("不設限")
RunFlag = False
TypeSelect = 0
#===================================APPinit

#===================================動作單元
def move_to(handle: HWND, x: int, y: int):
    wparam = 0
    lparam = y << 16 | x
    PostMessageW(handle, WM_MOUSEMOVE, wparam, lparam)


def left_down(handle: HWND, x: int, y: int):
    wparam = 0
    lparam = y << 16 | x
    PostMessageW(handle, WM_LBUTTONDOWN, wparam, lparam)


def left_up(handle: HWND, x: int, y: int):
    wparam = 0
    lparam = y << 16 | x
    PostMessageW(handle, WM_LBUTTONUP, wparam, lparam)


def scroll(handle: HWND, delta: int, x: int, y: int):
    move_to(handle, x, y)
    wparam = delta << 16
    p = POINT(x, y)
    ClientToScreen(handle, byref(p))
    lparam = p.y << 16 | p.x
    PostMessageW(handle, WM_MOUSEWHEEL, wparam, lparam)

def scroll_up(handle: HWND, x: int, y: int):
    scroll(handle, WHEEL_DELTA, x, y)


def scroll_down(handle: HWND, x: int, y: int):
    scroll(handle, -WHEEL_DELTA, x, y)
#===================================動作單元


#===================================系統動作
def Stop():
    global StopFuntion
    StopFuntion = True
    messagebox.showinfo("Alert", "Funtion stop")

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
    
#===================================按鈕funtion



#===================================資料存儲
    
def countset():
    global FightCount
    
    
    if CountEntry.get()== "" or CountEntry.get()== "0":
        FightCount = 0
        print("FightCount：",FightCount)
        fcset=("不設限")
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
#===================================驗證函式
def validate(P):
    #print(P)
    if str.isdigit(P) or P == '':
        return True
    else:
        return False
#===================================驗證函式
#=========================================刷方陣Funtion
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

 #   import sys
 #   if not windll.shell32.IsUserAnAdmin():
 #       windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
 #   import cv2
 #   handle = windll.user32.FindWindowW(None, "GBF")
 #   left_down(handle, 1234, 20)
 #   time.sleep(0.1)
 #   left_up(handle, 1234, 20)
 #   time.sleep(1)
 #   scroll_down(handle, 1000, 200)
#=========================================刷方陣Funtion
#=========================================刷轉世Funtion
def RunTLOscrept():
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
#=========================================刷轉世Funtion
#=========================================選擇執行方案
def RunGBFscrept():
    if TypeSelect == 0:
        RunFGscrept()
    elif TypeSelect == 1:
        RunTLOscrept()


#=========================================選擇執行方案
#===================================DBG 用
def AppDataCheck():
    HWNS = win32gui.FindWindow(None, "Skype")
    left, top, right, bottom = win32gui.GetWindowRect(HWNS)
    posStr1 = str(left).rjust(4)+','+str(top).rjust(4)+','+str(right).rjust(4)+','+str(bottom).rjust(4)
    print("AppPos: ", posStr1)     
    print("StopFuntion: ", StopFuntion)
    print("FightCount: ", FightCount)
    print("IntFightCount: ", IntFightCount)
    print("TypeSelect: ", TypeSelect)
    print("RunFlag: ", RunFlag)    
    
#===================================DBG 用     



#---------------------UI框架----------------------------------------------------------           
root = tk.Tk()
notebook=ttk.Notebook (root)
root.title('GBF_Scrept')
screenHeight=root.winfo_screenheight()
screenWidth=root.winfo_screenwidth()
w=600  #width
r=400  #height
x=200  #與視窗左上x的距離
y=300  #與視窗左上y的距離
root.geometry('%dx%d+%d+%d' % (w,r,x,y))
imgSave = ImageTk.PhotoImage(file='systemdata\icon\Save.dat')
imgLoad = ImageTk.PhotoImage(file='systemdata\icon\Load.dat')
imgHelp = ImageTk.PhotoImage(file='systemdata\icon\Heip.dat')
root.iconbitmap('systemdata\icon\ICON.dat')

#===================================Menu
filemenu=tk.Menu(root)
root.config(menu=filemenu)
mb1=tk.Menu(filemenu,tearoff=0)
mb2=tk.Menu(filemenu,tearoff=0)
mb3=tk.Menu(filemenu,tearoff=0)



mb1.add_command(label='  Save', image=imgSave, compound='left')
mb1.add_command(label='  Load', image=imgLoad, compound='left')
mb2.add_command(label='  Help', image=imgHelp, compound='left', command = OptionHelp)

filemenu.add_cascade(label=' 檔案 ',menu=mb1)
filemenu.add_cascade(label=' 設定 ',menu=mb2)
#===================================Menu


#===================================Setting頁面
setting= tk.Frame()
notebook.add(setting, text="setting")
b=tk.Button (setting, text="stopfuntion", command=Stop) 
b.grid(row=0,column=0)
#===================================Setting頁面

#===================================Run頁面
run= tk.Frame()
notebook.add(run, text="   run   ")
#===================================Run頁面

#===================================Debug頁面
debugger=tk.Frame()
notebook.add(debugger, text="debugger")

counttext = tk.Label(debugger,text="執行次數",font=("Algerian",12,"bold"),padx=1,pady=1)
counttext.grid(row=0,column=0)
CountEntry=0
vcmd = (root.register(validate), '%P')
CountEntry = tk.Entry(debugger,textvariable=CountEntry,validate='key',validatecommand=vcmd)
CountEntry.grid(row=0,column=1,padx=10,pady=10)

countset()

#框格
SelectBox = ttk.Combobox(debugger, values=['方陣','轉世'])
SelectBox.current(0)
SelectBox.grid(row=0,column=6)
SelectBox.bind('<<ComboboxSelected>>',typeset)


b=tk.Button (debugger, text="RunGBFscrept", command=RunGBFscrept, width=20)
b.grid(row=1,column=1,padx=5,pady=5)
b=tk.Button (debugger, text="stopfuntion", command=Stop, width=20) 
b.grid(row=2,column=1,padx=5,pady=5)
b=tk.Button (debugger, text="reset", command=reset, width=20) 
b.grid(row=3,column=1,padx=5,pady=5)
b=tk.Button (debugger, text="debug", command=AppDataCheck, width=20) 
b.grid(row=4,column=1,padx=5,pady=5)
b=tk.Button (debugger, text="set", command=countset, width=5) 
b.grid(row=0,column=3,padx=5,pady=5)
#===================================Debug頁面
notebook.pack (padx=10, pady=10, fill='both', expand=True)
root.mainloop()

#funtionclose=0
#print("GBF_Scrept")
#print("select 1 to run GBF_Scrept ,2 for get pointer for debug")
#while funtionclose == 0:
#
#    Choosetrancelate = input("what you want to do ? : ")    
#    if Choosetrancelate == "1":
#        runGBFscrept()
#    elif Choosetrancelate == "2":
#        GetGBFpointer()
#    elif Choosetrancelate == "exit" or Choosetrancelate == "Exit" or Choosetrancelate == "EXIT":
#        funtionclose=1
#    else:
#        os.system('cls')
#        print("invalid input")


#---------------------UI框架----------------------------------------------------------     

