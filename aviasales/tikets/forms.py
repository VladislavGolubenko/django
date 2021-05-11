from django import forms
from .models import Carrier

class ParametrForm(forms.Form):

    names_query = Carrier.objects.all()
    names_array = []
    for key in names_query:
        names_array.append([key, key])

    carriers_names = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        choices=names_array,
    )

    # def __init__(self, *args, **kwargs):
    #     super(ParametrForm, self).__init__(*args, **kwargs)
    #     self.fields['carriers_names'].widget.attrs['class'] = "select_input"

    departure = forms.BooleanField(initial=True, required=False, label='Показывать билеты с пересадками', widget=forms.CheckboxInput())

    # Принимаемые атрибуты
    # required=True/False - обязательное поле или нет
    # initial='изначальное значение'
    # empty_label='(Nothing)' - изначальное значение выпадающих списков. если NONE то первый элемент
    # widget - все что хотим применить к инпуту
