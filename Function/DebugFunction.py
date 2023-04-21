from threading import Thread
import os
import sys
import time
import Function.Foundation

class Debugfunction:
    #===================================debug
    def debugLog(self):
        print("#============================================================")
        print("StopFunction: ", Function.Foundation.StopFunction)
        print("Function1FightCount: ", Function.Foundation.Function1FightCount)
        print("TypeSelect: ", Function.Foundation.TypeSelect)
        print("RunFlag: ", Function.Foundation.RunFlag)
        print("WindowsHandle: ", Function.Foundation.WindowsHandle)