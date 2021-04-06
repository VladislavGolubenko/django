from django.contrib import admin

from .models import *

# class AirportAdmin(admin.ModelAdmin):
#     list_display = ('id_airport', 'city', 'airport_name', 'airport_code', 'adress', 'contact_phone')
#     list_display_links = ('id_airport', 'airport_name')  # какие поля будут ссылками
#     search_fields = ('city', 'airport_name', 'airport_code')  # по каким полям будет происходить поиск
#     # list_editable = ('')  # какие поля можно редактировать сразу в таблице
#     # list_filter = ('is_published', 'category')  # для вывода боковых фильтров вывода

admin.site.register(Airport)
admin.site.register(Order)
admin.site.register(Carrier)
admin.site.register(Plane)
admin.site.register(Tiket)
admin.site.register(Flights)
