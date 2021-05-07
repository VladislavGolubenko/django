from django import template
from tikets.models import *

register = template.Library()

@register.simple_tag()
def get_Flights():
    return Flights.objects.all()