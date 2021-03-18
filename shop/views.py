from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.

def index(request):
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod,range(1,nSlides), nSlides])
    params={'allProds':allProds}
    return render(request, "shop/index.html", params)
def about(request):
    return render(request, "shop/about.html")
def contact(request):
    return HttpResponse("This is shop-Contact ")
def tracker(request):
    return HttpResponse("This is shop-tracker ")
def search(request):
    return HttpResponse("This is shop-search ")
def productview(request):
    return HttpResponse("This is shop-productview")
def checkout(request):
    return HttpResponse("This is shop-checkout ")
def hotproducts(request):
    return HttpResponse("This is shop-Hotproducts ")