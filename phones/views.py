from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    i = request.GET.get("sort", "")
    print(i)
    template = 'catalog.html'
    if i == '':
        phones = Phone.objects.all()

    if i == 'min_price':
        phones = Phone.objects.all().order_by('price')

    if i == 'max_price':
        phones = Phone.objects.all().order_by('-price')

    if i == 'name':
        phones = Phone.objects.all().order_by('name')

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {
        'phone': phone,
    }
    return render(request, template, context)
