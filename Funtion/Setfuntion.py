
from threading import Thread
import os
import sys
import time
import Funtion.Foundation 
import UI.Call_MainUi

#===================================debug
def debugLog():
    print("StopFunction: ", StopFunction)
    print("FightCount: ", IntFightCount)
    print("TypeSelect: ", TypeSelect)
    print("RunFlag: ", RunFlag)

#====================================function
def RunFGscrept():
    if Funtion.Foundation.RunFlag == False:
        Funtion.Foundation.RunFlag = True
        Funtion.Foundation.StopFunction = False
        if Funtion.Foundation.IntFightCount == 0:
            #無限迴圈
            def GBFloop():
                while Funtion.Foundation.StopFunction == False:              
                    print(f"test run run run: 無上限") 
                    time.sleep(1)
                    print("stopfuntion=",Funtion.Foundation.StopFunction)
                    print("FightCount=",Funtion.Foundation.IntFightCount)
                Funtion.Foundation.RunFlag = False
        else:
            #有限迴圈
            def GBFloop():
                for i in range(Funtion.Foundation.IntFightCount):
                    C=i+1
                    TC=Funtion.Foundation.IntFightCount                
                    print(f"test run run run: {C}/{TC}")  
                    time.sleep(1)
                    print("stopfunction=",Funtion.Foundation.StopFunction)
                    print("FightCount=",Funtion.Foundation.IntFightCount)  
                    if Funtion.Foundation.StopFunction:
                        print('函数停止运行')
                        break
                Funtion.Foundation.RunFlag = False

        global functionthread
        functionthread = Thread(target=GBFloop)
        functionthread.setDaemon(True)
        functionthread.start()
        
    
    