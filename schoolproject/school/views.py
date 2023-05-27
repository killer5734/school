from webbrowser import get

from django.http import HttpResponse
from django.shortcuts import render
from . models import Product

# Create your views here.
def index(request):
    obj=Product.objects.all()
    return render(request,"index.html",{'result':obj})

