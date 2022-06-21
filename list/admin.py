from django.contrib import admin

# Register your models here.
from .models import list

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id',"title", 'cried_ad', 'upcried_ad' , 'is_bulishen' )
    list_display_links = ('id',"title")
    search_fields = ("title", "content")

admin.site.register(list, NewsAdmin)

