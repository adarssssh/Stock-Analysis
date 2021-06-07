import pandas_datareader as web
from plotly.offline import plot
import plotly.graph_objs as go

def DataSet(token, start, end):
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