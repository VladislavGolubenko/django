from django import template
from tikets.models import *

register = template.Library()

@register.simple_tag
def get_Flights():

    return Flights.objects.all()

# @register.simple_tag
# def get_maxcost():
#
#     return Flights.objects.all()
#
#     i = 0
#
#     for price in flights:
#         if i == 2:
#             if price[i] > price[i - 1]:
#                 max_price = price[i]
#         i += 1
#
#     return max_price