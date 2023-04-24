
from threading import Thread
import os
import sys
import time
import Function.Foundation

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
        print("StopFunction: ", Function.Foundation.StopFunction)
        print("Function1FightCount: ", Function.Foundation.Function1FightCount)
        print("TypeSelect: ", Function.Foundation.TypeSelect)
        print("RunFlag: ", Function.Foundation.RunFlag)    
    #====================================function
    def RunFGscrept(self):
        if Function.Foundation.RunFlag == False:
            Function.Foundation.RunFlag = True
            Function.Foundation.StopFunction = False
            if Function.Foundation.Function1FightCount == 0:
                #無限迴圈
                def GBFloop():
                    while Function.Foundation.StopFunction == False:
                        try:
                            print(f"test run run run: 無上限") 
                            time.sleep(1)
                            print("stopfuntion=",Function.Foundation.StopFunction)
                            print("Function1FightCount=",Function.Foundation.Function1FightCount)
                            Function.Foundation.RunFlag = False
                        except:
                            print("Function fail")
                            Function.Foundation.RunFlag = False
            else:
                #有限迴圈
                def GBFloop():
                    for i in range(Function.Foundation.Function1FightCount):
                        try:
                            C=i+1
                            TC=Function.Foundation.Function1FightCount                
                            print(f"test run run run: {C}/{TC}")  
                            time.sleep(1)
                            print("stopfunction=",Function.Foundation.StopFunction)
                            print("Function1FightCount=",Function.Foundation.Function1FightCount)  
                            if Function.Foundation.StopFunction:
                                break
                        except:
                            print("Function fail")
                            Function.Foundation.RunFlag = False
                    Function.Foundation.RunFlag = False
        
            global functionthread
            functionthread = Thread(target=GBFloop)
            functionthread.setDaemon(True)
            functionthread.start()
    
        
    
    