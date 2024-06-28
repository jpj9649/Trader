import yfinance as yf
import pandas as pd

# Signal generators moved to signals.py
from signals import * 
from plot import * 

# profits moved to finances.py
from finances import *

import pandas_ta as ta

#####################################
##
##         MAIN
##
#####################################

# Various tickers to pull data for    
ticker_list = ["AAPL", "NVDA", "GOOG", "META", "MSFT", "NXPI", "SLAB", "TSM", "INTC", "TXN", "FL", "DIS", "GOOS"]

#profit results in dict with ticker as key and profit as value
results = {}

# One at a time loop through each ticker from the above ticker list. Add any, remove any as needed
for ticker in ticker_list:

    # print('Ticker = {0}'.format(ticker))

    # dataF = yf.download(tickers = [ticker], start="2024-05-14", end="2024-06-24", interval='15m', prepost = 'TRUE') #YYYY=MM=DD
    # dataF = yf.download(tickers = [ticker],period='3mo') #YYYY=MM=DD
    # dataF = yf.download(tickers = [ticker],period='7d') #YYYY=MM=DD
    dataF = yf.download(tickers = [ticker], start="2024-05-01", end="2024-06-27", interval='5m')
    dataF.iloc[:,:]
    
    #init / define several variable in one line
    profit, share_cost, shares, signal = 0, 0, 0, [0]

    df = dataF

    # remove days without movement ie weekends
    df = df[df.High!=df.Low]
    df.reset_index(inplace=True, drop=False)

    # add bollinger bands to data table
    bb_len, bb_std = 25, 2.0
    df.ta.bbands(append = True, length = bb_len, std = bb_std)
    bb_len_std = '_'+str(bb_len)+'_'+str(bb_std)
    df[('bb_width'+bb_len_std)] = (df[('BBU'+bb_len_std)] - df[('BBL'+bb_len_std)]) / df[('BBM'+bb_len_std)]
    # df['bb_width'] = (df['BBU_10_1.5'] - df['BBL_10_1.5']) / df['BBM_10_1.5']

    # Add RSI to data table
    rsi_len = 14
    df.ta.rsi(append = True, length = rsi_len)

    # Add ATR to data table
    atr_len = 14
    df.ta.atr(append = True, low=df.Low, close = df.Close, high = df.High, length = atr_len)

    # plot if wanted
    showIt(df, str(bb_len_std), str(rsi_len))

    # signal.append(0)
    for i in range(1,len(dataF)): # cycle through each row of data (timestamps)
        df = dataF[i-1:i+1]

        # naive signal gen
        signal.append(signal_generator(df))



        if signal[-1] != 0:
            shares, profit, share_cost = gains(profit, signal[-1], shares, df.Close.iloc[-1], share_cost)

    dataF["signal"] = signal

    # dataF.signal.value_counts()

    print("Profit for {1}: ${0:.2f}".format(profit, ticker))

    # store ticker result into dict
    # Can access in debug console like this: 
    # ...results['AAPL']            returns below 4 elements ie
    #  {'profit': -12.00559201660164, 'No Signal': 1297, 'Sell Signal': 95, 'Buy Signal': 80}
    #  or ... 
    # ...results['AAPL']['profit']  returns only the profit element associate with AAPL ie -12
    # results['AAPL']['profit']
    # -12.00559201660164
    results[ticker] = { 
        "profit":profit, 
        "No Signal":dataF.signal.value_counts()[0],
        "Sell Signal":dataF.signal.value_counts()[1],
        "Buy Signal":dataF.signal.value_counts()[2],
    }
print(results) 