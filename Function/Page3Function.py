from threading import Thread
import os
import sys
import time
import Function.Foundation

#方陣頁面內容
#1.該模式為巡島
#2.巡島會依序從上到下打完，如果中途中斷，也會繼續往下執行 
#3.關卡開始，可選擇開場FA或是第一回合手動。
#5.隊伍可以指定X/Y方法，或是額外不選擇，僅使用前一場使用的隊伍
#6.腳本執行至關卡結束

class RunFunction3: