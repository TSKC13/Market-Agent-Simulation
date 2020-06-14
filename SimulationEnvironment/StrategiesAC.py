#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 17:20:38 2020

@author: boyuwang
"""
import numpy as np

DAILY_VOL    = 0.09276              # daily(-->TimeHorizon=100s) volatility
DAILY_VOLUME = 187760              # ADTV
TOTAL_SIZE   = int(DAILY_VOLUME * 0.1)   # shares to execute
EXEC_PERIOD  = 10                   # liquidation period


DIRECTION    = "sell"
ORDER_ID     = "strategy"

class Algo:  # base class
    def __init__(self):
        self.done = False
    
    def reset(self):
        self.__init__()
    
    def action(self, state):
        strategy_order = []
        return strategy_order, self.done


class myStrategy_demo1(Algo):
    
    __init__base = Algo.__init__
    
    def __init__(self, para1, para2):
        
        self.__init__base()
        '''strategy params'''
        self.para1 = para1
        self.para2 = para2
        self.done  = False
        self.is_limit = False
        ETA = 0.2/0.01/DAILY_VOLUME
        n = 900
        self.n = n
        self.T_i = np.array([i/n for i in range(n+1)])
        k = 0.01*DAILY_VOL/np.sqrt(ETA)
        self.X_i = list((np.exp(-k*self.T_i) - np.exp(k*self.T_i - 2*k))/(1-np.exp(-2*k))*TOTAL_SIZE)
        # self.n_i = [self.X_i[i + 1] - self.X_i[i] for i in range(n)]
        self.X_i.pop(0)


        self.next = 0

        
    def reset(self):
        
        self.__init__base()
        self.__init__(self.para1, self.para2)

    def action(self, state):
        ## for demenstration purpose
        strategy_order = []
        if state.current_time > (self.next+0.5)/self.n*99 and self.next < self.n:
            this_volume = max(int(state.strategy_record.position+TOTAL_SIZE-self.X_i[self.next]),0)
            strategy_order = [ORDER_ID, "market", DIRECTION, this_volume, 0]
            # print(self.X_i[self.next],  this_volume)
            self.next += 1
        remain = TOTAL_SIZE + state.strategy_record.position
        if state.current_time > 99.5 and remain != 0:
            strategy_order = [ORDER_ID, "market", DIRECTION, remain, 0]
        return [strategy_order], self.done

                        
                        
                      
                        
                        
                        
                        
