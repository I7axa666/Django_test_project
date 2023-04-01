import operator

from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', 'name')
    if sort == 'max_price':
        phones = Phone.objects.order_by('-price')

    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')
    else:
        phones = Phone.objects.order_by('name')

    template = 'catalog.html'

    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    phone = Phone.objects.filter(slug=slug)[0]
    context = {
        'phone': phone
    }
    return render(request, template, context)
