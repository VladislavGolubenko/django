from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import ParametrForm

from .models import *

def index(request):
    # news = News.objects.order_by('-created_at')
    # Если нужно вывести все без сортировки то .(all)

    title = 'Фильтры'

    return render(request, 'tikets/index.html', {})

def scroll(request):

    if request.method == 'POST':
        form = ParametrForm(request.POST)

        if form.is_valid() and form.is_bound:
            carriers_query=form.cleaned_data['carriers_names']
    else:
        form = ParametrForm()

    carrier = Carrier.objects.all()
    flights = Flights.objects.all()

    context = {
        'flights': flights,
        'title': 'Отображение',
        'carriers': carrier,
        'form':form,

    }

    return render(request, 'tikets/scroll.html', context=context)
