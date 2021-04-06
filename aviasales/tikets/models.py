from django.db import models

class Airport(models.Model):
    #id_airport
    # id = models.IntegerField(primary_key=True, verbose_name='ID')
    city = models.CharField(max_length=250, verbose_name='Город')
    airport_name = models.CharField(max_length=250, verbose_name='Название аэропорта')
    airport_code = models.CharField(max_length=10, verbose_name='Кодовое название аэропорта')
    adress = models.CharField(max_length=1000, verbose_name='Адресс аэропорта')
    contact_phone = models.IntegerField(verbose_name='Контактный телефон')

    def __str__(self):
        return self.airport_name

    class Meta:
        verbose_name = 'Аэропорт'
        verbose_name_plural = 'Аэропорты'
        ordering = ['city']


class Order(models.Model):
    #id_order
    # id = models.IntegerField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=25, verbose_name='Имя')
    surename = models.CharField(max_length=25, verbose_name='Фамилия')
    fathername = models.CharField(max_length=25, verbose_name='Отчество', blank=True)
    pasport = models.CharField(max_length=15, verbose_name='Серия/номер паспорта')
    phone = models.IntegerField(verbose_name='Номер телефона')

    def __str__(self):
        return self.pasport

    class Meta:
        verbose_name = 'Пассажир'
        verbose_name_plural = 'Пассажиры'
        ordering = ['surename']

class Carrier(models.Model):
    # id_carrier = models.IntegerField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=40, verbose_name='Название компании')
    contact_phone = models.IntegerField(verbose_name='Контактный номер перевозчика')
    adress = models.CharField(max_length=250, verbose_name='Адрес регистрации')
    logo = models.ImageField(upload_to='photos/%y/%m/%d/', verbose_name='логотип', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Авиакомпания'
        verbose_name_plural = 'Авиакомпании'
        ordering = ['name']


class Plane(models.Model):

    # id_plane = models.IntegerField(primary_key=True, verbose_name='ID')
    model_plane = models.CharField(max_length=20, verbose_name='Модель самолёта')
    places = models.IntegerField(verbose_name='Всего мест')
    vip_places = models.IntegerField(verbose_name='VIP мест', blank=True)
    vip_price = models.IntegerField(verbose_name='Стоимость vip мест', blank=True)
    bussines_places = models.IntegerField(verbose_name='Кол-во бизнесс мест', blank=True)
    bussines_price = models.IntegerField(verbose_name='Стоимость бизнесс мест', blank=True)
    econom = models.IntegerField(verbose_name='Кол-во эконом мест')
    econom_price = models.IntegerField(verbose_name='Стоимость эконом мест')
    window_upsale = models.IntegerField(verbose_name='Доплата за место у окна', blank=True)
    trunk_sale = models.IntegerField(verbose_name='Доплата за багаж')
    carrier_id = models.ForeignKey('Carrier', on_delete=models.PROTECT, null=True, verbose_name='Перевозчик')

    def __str__(self):
        return self.model_plane

    class Meta:
        verbose_name = 'Самолёт'
        verbose_name_plural = 'Самолёты'
        ordering = ['model_plane']

class Tiket(models.Model):

    # id_tiket = models.IntegerField(primary_key=True, verbose_name='ID')
    flight_id = models.ForeignKey('Flights', on_delete=models.PROTECT, null=True, verbose_name='Рейс')
    order_id = models.ForeignKey('Order', on_delete=models.PROTECT, null=True, verbose_name='Заказчик')
    place = models.IntegerField(verbose_name='Номер места')
    purchase_date = models.DateTimeField(auto_now=True, verbose_name='Дата покупки билета')
    depatrure_date = models.DateTimeField(auto_now=False, verbose_name='Дата вылета')
    trunk = models.BooleanField(verbose_name='Наличие багажа')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
        ordering = ['purchase_date']


class Flights(models.Model):
    # id_flights = models.IntegerField(primary_key=True, verbose_name='ID')
    departure_airport = models.ForeignKey('Airport', on_delete=models.PROTECT, related_name='departure_airport', null=True, verbose_name='Точка вылета')
    arrival_point_airport = models.ForeignKey('Airport', on_delete=models.PROTECT, related_name='arrival_point_airport', null=True, verbose_name='Аэропорт назначения', blank=True)
    transfer_point = models.ForeignKey('Airport', on_delete=models.PROTECT, related_name='transfer_point', null=True, verbose_name='Аэропорт пересадки')
    departure_time = models.DateTimeField(auto_now_add=False, verbose_name='Время вылета')
    arrival_time = models.DateTimeField(auto_now_add=False, verbose_name='Время прибытия')
    plane_id = models.ForeignKey('Plane', on_delete=models.PROTECT, null=True, verbose_name='Самолёт')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'
        ordering = ['departure_time']
