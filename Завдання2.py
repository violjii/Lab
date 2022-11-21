# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 16:08:58 2022

@author: ПК
"""
import numpy as np
from scipy.interpolate import interp1d
from scipy.integrate import odeint
import matplotlib.pyplot as plt

a=0.5
b=0.3
S0=990000
I0=7000
N=1000000
R0=3000
def s(S,t):
    return -a*S

def I_(I,t):
    return (a*S0*np.exp(-a*t)-b*I)


x=np.linspace(0,30)
S=odeint(s,S0,x)
I=odeint(I_,I0,x)
R=[R0+N-S[j][0]-I[j][0] for j in range(len(S))]
plt.plot(x,R)
plt.plot(x,S)
plt.plot(x,I)



