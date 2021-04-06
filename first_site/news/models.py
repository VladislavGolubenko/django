from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок') #verbose_name - альтернативное понятное имя, которое мы будем выводить
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    is_published = models.BooleanField(default=True, verbose_name='Опубликованно', blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    #МЕТАКЛАСС ДЛЯ ИЗМЕНЕНИЯ ИМЕН В АДМИНКЕ И СОРТИРОВКИ КАК В АДМИНКЕ, ТАК И В ПРИЛОЖЕНИИ
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Заголовок категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
