"""first_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# импортируем settings & static для отладки вывода импортируемых изображений 
from django.conf import settings
from django.conf.urls.static import static 

from django.contrib import admin
from django.urls import path, include #импортируем виды чтоб их постоянно не подключать и избежать проблемы при переносе проекта
#Для этого создаем в самом приложении файл urls.py

# from news.views import controller_name  подключаем контролеры*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
]

#Для вывода изображений в отладочном режиме
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
