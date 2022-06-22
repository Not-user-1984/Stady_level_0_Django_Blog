from django.contrib import admin

# Register your models here.
from .models import list,Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id',"title", 'Category','cried_ad', 'upcried_ad' , 'is_bulishen' )
    list_display_links = ('id',"title")
    search_fields = ("title", "content")
    list_editable = ('is_bulishen',)
    list_filter = ('is_bulishen', 'Category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_link = ('id', 'title')
    search_fields = ("title", "content")

admin.site.register(list, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

