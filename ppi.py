# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:17:28 2024

@author: IppearPeng
"""

import numpy as np
import matplotlib.pyplot as plt

def ppi(x,y,inch):
    return (x**2+y**2)**0.5/inch

size=np.linspace(1,110,num=219)
qhd=ppi(2560,1440,size)

plt.plot(size,qhd)

#push test