import pandas_datareader as web
from plotly.offline import plot
import plotly.graph_objs as go
import datetime as dt

def DataSet(token):

    end = dt.datetime.now()
    day = dt.timedelta(days=365)
    start = end - day

    data = web.DataReader(token, 'yahoo', start, end)
    
    graph = [go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], name = 'market data')]
    
    layout = {
        'title': f'{token} live share price evolution',
        'yaxis_title': 'Stock Price (USD per Shares)'
    }

    plot_div = plot({'data': graph, 'layout': layout}, 
                    output_type='div')

    my_formater = "{0:.2f}"

    current = my_formater.format(data['Close'][-1])
    high = my_formater.format(data['High'].max())
    low = my_formater.format(data['Low'].min())

    # data = [current price, highest, lowest, plot]
    data = [current, high, low, plot_div]

    return data

def priceData():
    end = dt.datetime.now()
    day = dt.timedelta(days=1)
    start = end - day

    my_formater = "{0:.2f}"

    data = []
    token = ['TSLA', 'AAPL', 'GOOG', 'FB']

    for tkn in token:
        webData = web.DataReader(tkn, 'yahoo', start, end)
        data.append(my_formater.format(webData['Close'][-1]))


    print(data)
    return data