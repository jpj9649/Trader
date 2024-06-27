# Signals
import pandas as pd
import pandas_ta as ta

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
##             2. MA
#####################################
# can be exponential, simple, or RSI moving average depending on the type str, t, that is passed in
# l is the lenth of the moving avg
def ma(d: dict, l: int, t: str):

    string = t+'-MA_'+str(l)
    if t == 'S':
        d[string] = ta.sma(d.Close,length=l)
    elif t == 'E':
        d[string] = ta.ema(d.Close,length=l)
    elif t == 'RSI':
        d[string] = ta.rsi(d.Close,length=l)
    else:
        print("Invalid moving average")
        quit()

    return d

#####################################
##             3. Bollinger bands
#####################################
def bb(d: dict, l: int, sigma: float):

    string = 'BB_'+str(l)+'_'+str(sigma)
    d[string] = ta.bbands(d.Close, length = l, std = sigma)

    return d

    