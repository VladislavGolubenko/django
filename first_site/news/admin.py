from django.contrib import admin

from .models import * #Импортируем модели которые будем использовать в админке


#Для вывода выбранных параметров создаем новую подмодель
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title') #какие поля будут ссылками
    search_fields = ('title', 'content') #по каким полям будет происходить поиск
    list_editable = ('is_published',) #какие поля можно редактировать сразу в таблице
    list_filter = ('is_published', 'category')# для вывода боковых фильтров вывода

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',) #если только один элемент, то в конце ставится запятая. Т.к это картеж иначе воспринимается как строка

#регистрируем модели (сначала основную, а потом подмодель)
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
