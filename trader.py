import yfinance as yf
import pandas as pd

# Signal generators moved to signals.py
from signals import * 

# profits moved to finances.py
from finances import *


# for 15minute interval, the history limitation is 60 days
# dataF = yf.download(tickers = ["AAPL", "NVDA", "GOOG", "META", "MSFT"], start="2024-06-06", end="2024-06-16", interval='15m', prepost = 'TRUE') #YYYY=MM=DD
# dataF = yf.download(tickers = ["AAPL"], start="2024-05-14", end="2024-06-16", interval='15m', prepost = 'TRUE') #YYYY=MM=DD
# dataF = yf.download("EURUSD=X",tickers = ["AAPL", "NVDA", "GOOG", "META", "MSFT"], start="2024-06-06", end="2024-06-16", interval='15m') #YYYY=MM=DD
# dataF.iloc[:,:]
#dataF.Open.iloc



#####################################
##
##         Signal Generator
##
#####################################
##              NAIVE
#####################################
# Signal generator 1 - naive
# def signal_generator(df):
#     open = df.Open.iloc[-1]
#     close = df.Close.iloc[-1]
#     previous_open = df.Open.iloc[-2]
#     previous_close = df.Close.iloc[-2]

#     #bearish - sell signal
#     if(open>close and previous_open<previous_close and close<previous_open and open>=previous_close):
#         return 1

#     #bullish - buy signal
#     elif(open<close and previous_open>previous_close and close>previous_open and open<=previous_close):
#         return 2
    
#     else: #no signal
#         return 0


#####################################
##
##               Gains
##
#####################################
# compute the gains from the buy / sell signals triggered buy the signal generator
# def gains(profit: float, sig: int, shares: int, close_price: float, share_cost: float):

#     if sig == 2: # sig = 2 is a buy signal
#         shares += 1 # add a share to our held share counter

#         # for FIRST share we purchase, our avg share price is simply the close_price
#         if (shares == 1): 

#             share_cost = close_price
#             print(" BUY: First Share bought at {0:.5}".format(share_cost))

#         # for additional shares we purchase after the first, our avg share price is weighted accordingly
#         if (shares > 1):

#             share_cost = (share_cost * (shares - 1)/(shares) + close_price * (1/shares))
#             print(" BUY: Buying share #{0} at ${1:.5}\t Avg price at ${2:.5}".format(shares,close_price,share_cost))

        
#     if sig == 1: # sig = 1 is a sell signal
#         if shares > 0: # Check if we have a share(s) to sell

#             profit = profit + shares * (close_price - share_cost) # sell all held shares when sell signal is triggered
#             print("SELL: {0} Share(s) at avg $/share {1:.5} sold for ${2:.5} to make profit: ${3:0.2}".format(shares,share_cost,close_price,shares * (close_price - share_cost)))

#             shares = 0 # reset held shares to 0 since we've liquidated our positions


#     # print("{0} Share(s)\navg $/share {1}".format(shares,profit))
#     return shares, profit, share_cost




#####################################
##
##         MAIN
##
#####################################

# Various tickers to pull data for    
ticker_list = ["AAPL", "NVDA", "GOOG", "META", "MSFT"]

#profit results in dict with ticker as key and profit as value
results = {}

# dataF = yf.download(tickers = ["AAPL"], start="2024-05-14", end="2024-06-16", interval='15m', prepost = 'TRUE') #YYYY=MM=DD
# dataF = yf.download("EURUSD=X",tickers = ["AAPL", "NVDA", "GOOG", "META", "MSFT"], start="2024-06-06", end="2024-06-16", interval='15m') #YYYY=MM=DD

# One at a time loop through each ticker
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