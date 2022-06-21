from turtle import title
from django.shortcuts import render
# Create your views here
from .models import list


def index(request):
    ist = list.objects.all()
    return render(request, 'list/index.html',{'List': ist, 'title': 'список новостей'})


