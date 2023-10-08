from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    catalog = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort == 'name':
        catalog = catalog.order_by('name')
    if sort == 'min_price':
        catalog = catalog.order_by('price')
    if sort == 'max_price':
        catalog = catalog.order_by('-price')
    context = {'phones': [c for c in catalog]}
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
