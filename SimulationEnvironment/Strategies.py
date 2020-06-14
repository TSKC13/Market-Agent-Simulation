#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 17:20:38 2020

@author: boyuwang
"""

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

    def reset(self):
        
        self.__init__base()
        self.__init__(self.para1, self.para2)

    def action(self, state):
        ## for demenstration purpose
        vol_per_order = self.para1
        if not self.done:
            time_prop = (0.01 * state.time_horizon + state.current_time) / state.time_horizon
            rem_qty = TOTAL_SIZE + state.strategy_record.position
            # print(rem_qty)
            if rem_qty > vol_per_order:
                this_order_volume = min(
                    vol_per_order * int((TOTAL_SIZE * time_prop + state.strategy_record.position) / vol_per_order),
                    rem_qty)
            else:
                this_order_volume = rem_qty

            if this_order_volume > 0:
                strategy_order = [ORDER_ID, "market", DIRECTION, this_order_volume, 0]
            else:
                strategy_order = []
        else:
            strategy_order = []
        
        return [strategy_order], self.done

                        
                        
                      
                        
                        
                        
                        
