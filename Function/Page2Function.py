from threading import Thread
import os
import sys
import time
import Function.Foundation

#1T轉世頁面內容
#1.需要向下尋找轉世的item
#2.要找到指定的關卡item
#3.進入關卡後分成3頁面 左中右 透過左右按鈕切畫面
#4.怪物以轉世關卡分類
#5.隊伍可以指定X/Y方法，或是額外不選擇，僅使用前一場使用的隊伍
#6.如果遇到意外 無法執行1T完成關卡 則直接攻擊直到關卡結束

class RunFunction2: