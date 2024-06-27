# Auto Trader
Use finance APIs to download stock market exchange history and back test buy-sell signal generators.

## Description
Currently using `yfinance` as a finance API to download ticker data. Our signal generators produce buy and sell remarks by employing various strategies

## Gameplan
- [ ] identify promising strategies on historical finance data
    - returns good profit per investment ratio
- [ ] Verify trading & commissions laws and regulations
    - trade limits
    - brokerage costs
    - tax caveats
- [ ] Enroll in subscription service to place orders
    - Binance
    - Alpaca
    - Interactive Brokers
    - TD Ameritrade
    - Oanda

### Strategy
-------
Buy-sell signal strategies
 - [x] **Naive**
    - *bullish*
        - open < close
        - previous_open > previous_close
        - close > previous_open
        - open <= previous_close
    - *bearish*
        - open > close
        - previous_open < previous_close
        - close < previous_open
        - open >= previous_close

 - [ ] Simple Moving Average (SMA)
    - history is linearly weighed, proportionally to is age
 - [ ] Exponential Moving Average (EMA)
    - recent history is exponentially weighed, history vanishes exponentially with age
 - [ ] Hybrid Moving Average (hMA)
 - [ ] Stochastics
 - [ ] Stochastics

### History
June 25th, 2024 - Conception of Idea

June 26th, 2024 - Initial commit

### Authors
-------
Jesse Judd - M.S.E UT Austin, B.S.uE RIT, A.S.E MCC, minor in mathematics

Collin Shelanskey - Full voicemail, big funny guy, more college credits than a senior valedictorian




