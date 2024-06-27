import yfinance as yf
import pandas as pd

# Signal generators moved to signals.py
from signals import * 

# profits moved to finances.py
from finances import *

#####################################
##
##         MAIN
##
#####################################

# Various tickers to pull data for    
ticker_list = ["AAPL", "NVDA", "GOOG", "META", "MSFT"]

#profit results in dict with ticker as key and profit as value
results = {}

# One at a time loop through each ticker from the above ticker list. Add any, remove any as needed
for ticker in ticker_list:

    print('Ticker = {0}'.format(ticker))

    dataF = yf.download(tickers = [ticker], start="2024-05-14", end="2024-06-16", interval='15m', prepost = 'TRUE') #YYYY=MM=DD
    dataF.iloc[:,:]
    
    #init / define several variable in one line
    profit, share_cost, shares, signal = 0, 0, 0, [0]

    # signal.append(0)
    for i in range(1,len(dataF)):
        df = dataF[i-1:i+1]
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