from django.shortcuts import render
from . import weatherCrawler as crawler
from django.utils import timezone

def home(request):
    weather = crawler.getWeather()
    hour = timezone.localtime().hour
    time='none'
    if hour<6:
        time='night'
    elif hour<10:
        time='morning'
    elif hour<17:
        time='daytime'
    elif hour<20:
        time='sunset'
    else:
        time='night'

    request.session['time'] = time
    request.session['weather'] = weather
    return render(request, 'mainpage.html', {"weather":weather, 'time':time})
