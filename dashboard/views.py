from django.shortcuts import render
from .models import *

def index(request):
    data = CountryData.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'dashboard/index.html', context)


def pie(request):
    datas = CountryData.objects.all()
    context = {
        'datas': datas,
    }
    return render(request, 'dashboard/pie.html', context)


def line(request):
    datas = CountryData.objects.all()
    context = {
        'datas': datas,
    }
    return render(request, 'dashboard/line.html', context)


def doughnut(request):
    datas = CountryData.objects.all()
    context = {
        'datas': datas,
    }
    return render(request, 'dashboard/doughnut.html', context)


