from threading import Thread
import os
import sys
import time
import Function.Foundation

#方陣速刷頁面內容
#1.該模式為接外放
#2.接外放有兩種模式可以選擇，1T mode 及 貢獻mode 
#3.選擇要刷的方陣 透過twitterapi找尋房間
#5.隊伍可以指定X/Y方法，或是額外不選擇，僅使用前一場使用的隊伍
#6.貢獻mode 可以指定貢獻度 若達到目標則跳出主畫面
#7.1T mode 執行完指定攻擊方式 完成後跳出主畫面
#8.如果遇到關卡滿載，處理以下事件
#8-1.救援數最大3，每10秒檢測一次關卡數量
#8-2.總數量達到最大，回收所有獎勵直到沒有領取按鈕出現

class RunFunction4: