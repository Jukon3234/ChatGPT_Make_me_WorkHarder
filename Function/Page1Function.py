
from threading import Thread
import os
import sys
import time
import Function.Foundation

class RunFunction:
    #===================================debug
    def debugLog(self):
        print("StopFunction: ", StopFunction)
        print("Function1FightCount: ", Function1FightCount)
        print("TypeSelect: ", TypeSelect)
        print("RunFlag: ", RunFlag)    
    #====================================function
    def RunFGscrept(self):
        if Funtion.Foundation.RunFlag == False:
            Funtion.Foundation.RunFlag = True
            Funtion.Foundation.StopFunction = False
            if Funtion.Foundation.Function1FightCount == 0:
                #無限迴圈
                def GBFloop():
                    while Funtion.Foundation.StopFunction == False:
                        try:
                            print(f"test run run run: 無上限") 
                            time.sleep(1)
                            print("stopfuntion=",Funtion.Foundation.StopFunction)
                            print("Function1FightCount=",Funtion.Foundation.Function1FightCount)
                            Funtion.Foundation.RunFlag = False
                        except:
                            print("Function fail")
                            Funtion.Foundation.RunFlag = False
            else:
                #有限迴圈
                def GBFloop():
                    for i in range(Funtion.Foundation.Function1FightCount):
                        try:
                            C=i+1
                            TC=Funtion.Foundation.Function1FightCount                
                            print(f"test run run run: {C}/{TC}")  
                            time.sleep(1)
                            print("stopfunction=",Funtion.Foundation.StopFunction)
                            print("Function1FightCount=",Funtion.Foundation.Function1FightCount)  
                            if Funtion.Foundation.StopFunction:
                                break
                        except:
                            print("Function fail")
                            Funtion.Foundation.RunFlag = False
                    Funtion.Foundation.RunFlag = False
        
            global functionthread
            functionthread = Thread(target=GBFloop)
            functionthread.setDaemon(True)
            functionthread.start()
    
        
    
    