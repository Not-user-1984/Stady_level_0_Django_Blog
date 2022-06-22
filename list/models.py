from ast import Try
from tabnanny import verbose
from django.db import models


# Create your models here.
class list(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='контент')
    cried_ad = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    upcried_ad = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='Фото')
    is_bulishen = models.BooleanField(default=True, verbose_name='Опубликовано')
    Category = models.ForeignKey('Category', on_delete=models.PROTECT, null= True,verbose_name= "Категория" )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['upcried_ad']

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name= "Наименование категории")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name ='Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
