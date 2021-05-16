from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import ParametrForm, BuyForm, FormFindTiket
from .filters import FlightFilter

from .models import *

def index(request):
    # news = News.objects.order_by('-created_at')
    # Если нужно вывести все без сортировки то .(all)

    if request.method == 'POST':

        form = FormFindTiket()

        # form = FormFindTiket(request.POST)
        #
        # if form.is_valid() and form.is_bound:
        #
        #     departure_place = form.cleaned_data['departure_place']
        #     arrivial_place = form.cleaned_data['arrivial_place']
        #     departure_date = form.cleaned_data['departure_date']
        #
        #     response = redirect('view_tikets/{0}/{1}/{2}'.format(departure_place, arrivial_place, departure_date))
        #     return response


    else:
        form = FormFindTiket()

    context = {
        'form': form,
    }

    return render(request, 'tikets/index.html', context=context)

def scroll(request):

    if request.method == 'POST':

        form = FormFindTiket(request.POST)

        if form.is_valid() and form.is_bound:

            airport_query = Airport.objects.all()

            departure_place = form.cleaned_data['departure_place']
            arrivial_place = form.cleaned_data['arrivial_place']
            departure_date = form.cleaned_data['departure_date']
            departure_date = str(departure_date)
            request.session['departure_date'] = departure_date

            for airport in airport_query:
                if departure_place == airport.city:
                    departure_place_id = airport.pk
                    request.session['departure_place_id'] = departure_place_id

                if arrivial_place == airport.city:
                    arrivial_place_id = airport.pk
                    request.session['arrivial_place_id'] = arrivial_place_id

    else:
        form = FormFindTiket()


    carrier = Carrier.objects.all()

    departure_place_id = request.session.get('departure_place_id')
    arrivial_place_id = request.session.get('arrivial_place_id')
    departure_date = request.session.get('departure_date')

    # if departure_date == None:
    print(departure_place_id, arrivial_place_id, departure_date)
    flights = Flights.objects.filter(departure_airport=departure_place_id, arrival_point_airport=arrivial_place_id, departure_time__gte=departure_date)




    filter = FlightFilter(request.GET, queryset=flights)

    cost = []
    for flight in flights:
        cost.append(flight.econom_price)

    maxcost = max(cost)

    context = {
        'flights': flights,
        'title': 'Отображение',
        'carriers': carrier,
        'form': form,
        'filter': filter,
        'maxcost': maxcost,
        'mincost': 0,
        'from': 0,
        'to': 500,
    }
    # query = Flights.objects.all()
    # for objectvar in query:
    #     print(objectvar.plane_id.places)

    return render(request, 'tikets/scroll.html', context=context)

def buy_tiket(request, id_flight):

    flights = Flights.objects.filter(pk=id_flight)

    if request.method == 'POST':
        form = BuyForm(request.POST)

    else:
        form = BuyForm()

    context = {
        'flights': flights,
        'form': form,
        'id_flight': id_flight,
    }


    return render(request, 'tikets/buy_tiket.html', context = context)

