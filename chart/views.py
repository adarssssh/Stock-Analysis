from django.shortcuts import render
import datetime as dt

from .dataset import DataSet
from .model import prediction

# Create your views here.
def chartdata(request):
    return render(request, 'home.html', {})

def stockdata(request):
    print(request.POST['token'])
    token = request.POST['token'].upper()
    start = request.POST['start']
    end = request.POST['end']

    data = DataSet(token,start,end)
    # data = [current price, highest, lowest, plot]

    pred = prediction(token,start,end)

    context = {
        'current': data[0],
        'highest': data[1],
        'lowest': data[2],
        'plt': data[3],
        'pred': pred,
    }

    return render(request, 'chart.html', context)