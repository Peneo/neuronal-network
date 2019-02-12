# -*- coding:utf-8 -*-
# author peneo
# peneo Rulkov simulation
import numpy as np
import matplotlib.pyplot as plt
import math as math

class Rulkov():
    def __init__(self, n):
        self.n = n
        ##--------------------------------------------------
        # n=10000;#iretation steps
        x=np.zeros((self.n,1));
        y=np.zeros((self.n,1));
        # print(x.shape)
        ## initial value------------------------------------
        x[0,0]=-1;
        y[0,0]=-2.8;#matlab the label is start from 0
        # print(x[0,0])
        ##--------------------------------------------------
        for i in range(self.n-1):
            x[i+1,0]=4.1/(1+x[i,0]*x[i,0])+y[i,0]+0.001;
            y[i+1,0]=y[i,0]-0.001*x[i,0]-0.001;
        self.v=-50*x/(1-math.sqrt(4.1));

    def show(self):
        ##--------------------------------------------------
        plt.plot(self.v);
        plt.show();
