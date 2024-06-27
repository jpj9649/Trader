# Signals
import pandas as pd

#####################################
##
##         Signal Generator
##
#####################################

#####################################
##             1. NAIVE
#####################################
# Signal generator 1 - naive
def signal_generator(df):
    open = df.Open.iloc[-1]
    close = df.Close.iloc[-1]
    previous_open = df.Open.iloc[-2]
    previous_close = df.Close.iloc[-2]

    #bearish - sell signal
    if(open>close and previous_open<previous_close and close<previous_open and open>=previous_close):
        return 1

    #bullish - buy signal
    elif(open<close and previous_open>previous_close and close>previous_open and open<=previous_close):
        return 2
    
    else: #no signal
        return 0
    

#####################################
##             2. SMA
#####################################

#####################################
##             2. EMA
#####################################