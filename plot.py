import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime

def showIt(df:dict, bb: str, rsi: str):

    fig = make_subplots(rows=1, cols=1)

    fig.add_trace(go.Candlestick(x = df.index,
                                open = df['Open'],
                                high = df['High'],
                                low = df['Low'],
                                close = df['Close'],
                                ),
                                row = 1, col = 1)

    fig.add_trace(go.Scatter(x = df.index,
                                y = df[('BBL'+bb)],
                                line=dict(color='green', width=1),
                                name='BBL'),
                                row = 1, col = 1)
    
    fig.add_trace(go.Scatter(x = df.index,
                                y = df[('BBU'+bb)],
                                line=dict(color='green', width=1),
                                name='BBU'),
                                row = 1, col = 1)
    
    # fig.add_trace(go.Scatter(x = df.index,
    #                             y = df[('RSI_'+rsi)],
    #                             line=dict(color='green', width=2),
    #                             name='RSI'),
    #                             row = 2, col = 1)
    
    fig.update_layout(width=1200, height=800, sliders=[],
                      yaxis_title='Stock',
                      xaxis_title='time')
    
    fig.show()
    
    

