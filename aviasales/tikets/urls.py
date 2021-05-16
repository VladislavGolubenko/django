from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('view_tikets/', scroll, name='view_tikets'),
    path('buy_tiket/<int:id_flight>/', buy_tiket, name='buy_tiket'),
# path('view_tikets/<slug:departure_place>/<slug:arrivial_place>/<slug:departure_date>', scroll, name='view_tikets'),
]
