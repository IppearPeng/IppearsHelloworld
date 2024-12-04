# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 15:43:59 2023

@author: IppearPeng
"""

import threading
import time

def func(event):
    while True:
        time.sleep(1)
        print("thread is Running!")
        if event.is_set():
            print("thread is Ended!")
            raise ValueError("thread is Ended!")
    return None

def threading_add(fun,e):
    global t
    t=threading.Thread(target=fun,args=(e,))
#    t.daemon=True
    t.start()

event=threading.Event()

threading_add(func,event)
