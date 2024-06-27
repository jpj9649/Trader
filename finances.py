# finances.py

#####################################
##
##               Gains
##
#####################################
# compute the gains from the buy / sell signals triggered buy the signal generator
def gains(profit: float, sig: int, shares: int, close_price: float, share_cost: float):

    if sig == 2: # sig = 2 is a buy signal
        shares += 1 # add a share to our held share counter

        # for FIRST share we purchase, our avg share price is simply the close_price
        if (shares == 1): 

            share_cost = close_price
            # print(" BUY: First Share bought at {0:.5}".format(share_cost))

        # for additional shares we purchase after the first, our avg share price is weighted accordingly
        if (shares > 1):

            share_cost = (share_cost * (shares - 1)/(shares) + close_price * (1/shares))
            # print(" BUY: Buying share #{0} at ${1:.5}\t Avg price at ${2:.5}".format(shares,close_price,share_cost))

        
    if sig == 1: # sig = 1 is a sell signal
        if shares > 0: # Check if we have a share(s) to sell

            profit = profit + shares * (close_price - share_cost) # sell all held shares when sell signal is triggered
            # print("SELL: {0} Share(s) at avg $/share {1:.5} sold for ${2:.5} to make profit: ${3:0.2}".format(shares,share_cost,close_price,shares * (close_price - share_cost)))

            shares = 0 # reset held shares to 0 since we've liquidated our positions


    # print("{0} Share(s)\navg $/share {1}".format(shares,profit))
    return shares, profit, share_cost