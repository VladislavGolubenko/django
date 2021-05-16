from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from .models import *
from django.contrib.admin.widgets import AdminDateWidget

from django import forms
from django.contrib.admin import widgets



class ParametrForm(forms.Form):

    names_query = Carrier.objects.all()
    names_array = []
    for key in names_query:
        names_array.append([key, key])

    carriers_names = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        choices=names_array,
    )


    departure = forms.BooleanField(initial=True, required=False, label='Показывать билеты с пересадками', widget=forms.CheckboxInput())

    # Принимаемые атрибуты
    # required=True/False - обязательное поле или нет
    # initial='изначальное значение'
    # empty_label='(Nothing)' - изначальное значение выпадающих списков. если NONE то первый элемент
    # widget - все что хотим применить к инпуту

class BuyForm(forms.Form):

    names = Flights.objects.all()
    name = forms.CharField()
    surename = forms.CharField()
    fathername = forms.CharField()
    phone = forms.IntegerField()
    pasport = forms.CharField()

class FormFindTiket(forms.Form):

    departure_place = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-2 mr-sm-2',
                'placeholder': 'Откуда',
            }
        ),
    )

    arrivial_place = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-2 mr-sm-2',
                'placeholder': 'Куда',
            }
        ),
    )






    departure_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Когда',
            }
        ),
    )


