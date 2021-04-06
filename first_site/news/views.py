from django.shortcuts import render
from django.http import HttpResponse



from .models import *

def index(request):

    news = News.objects.order_by('-created_at')
    title = 'Список новостей'
    return render(request, 'news/index.html', {'news': news, 'title': title})


