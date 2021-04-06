from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def index(request):
    # news = News.objects.order_by('-created_at')
    # Если нужно вывести все без сортировки то .(all)

    title = 'Aviasales'

    return render(request, 'tikets/index.html', {})

def scroll(request):

    flights = Flights.objects.all()
    title = 'Aviasales'

    return render(request, 'tikets/scroll.html', {'flights': flights, 'title': title})
