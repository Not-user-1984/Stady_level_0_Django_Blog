from multiprocessing import context
from turtle import title
from django.shortcuts import render
# Create your views here
from .models import list


def index(request):
    ist = list.objects.all()
    context = {
        'List': ist,
        'title': 'список новостей'
        }
    return render(request, template_name='list/index.html',context = context)


