# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate  as inter
import scipy.integrate as integrate




speed=[25,35,45,30,60,120,100,100,70,75,80,65]
t= np.linspace(0,11,12)
t1= np.linspace(0,11,120)
print("Массив часу:",t)

f= inter.interp1d(t, speed, kind='cubic')
cubic=f(t1)
f1=lambda x:f(x)

f= inter.interp1d(t, speed, kind='quadratic')
quadratic=f(t1)
f2=lambda x:f(x)

s1=[integrate.quad(f1,0 ,t[i])[0] for i in range(12)]
inter_s1=inter.interp1d(t, s1, kind='quadratic')(t1)

s2=[integrate.quad(f2,0 ,t[i])[0] for i in range(12)]
inter_s2=inter.interp1d(t, s2, kind='linear')(t1)

fig=plt.figure()

ax1=fig.add_subplot(2,2,1)
ax3=fig.add_subplot(2,2,2)
ax2=fig.add_subplot(2,2,3)
ax4=fig.add_subplot(2,2,4)

ax1.plot(t,speed)
ax1.plot(t1,cubic)
ax2.plot(t,s1,linestyle="dashed")
ax2.plot(t1,inter_s1)

ax3.plot(t,speed)
ax3.plot(t1,quadratic)
ax4.plot(t,s2,linestyle="dashed")
ax4.plot(t1,inter_s2)