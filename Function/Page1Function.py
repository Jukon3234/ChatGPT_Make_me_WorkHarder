
from threading import Thread
import os
import sys
import time
import Function.Foundation

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
    
        
    
    