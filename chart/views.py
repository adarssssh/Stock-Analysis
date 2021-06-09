from django.shortcuts import render
import datetime as dt

from .dataset import DataSet
from .dataset import priceData
from .model import prediction

# Create your views here.
def chartdata(request):
    price = priceData()
    context = {
        'tsla': price[0],
        'aapl': price[1],
        'goog': price[2],
        'fb': price[3]
    }
    return render(request, 'home.html', context)

def stockdata(request):
    print(request.POST['token'])
    token = request.POST['token'].upper()

    data = DataSet(token)
    # data = [current price, highest, lowest, plot]

    pred = prediction(token)

    context = {
        'current': data[0],
        'highest': data[1],
        'lowest': data[2],
        'plt': data[3],
        'pred': pred,
    }

    return render(request, 'chart.html', context)