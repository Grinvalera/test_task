from django.shortcuts import render

from .models import Car, News, Contact


def main(request):
    return render(request, 'main_html.html', context={})


def car_mazda(request):

    mazda = Car.objects.filter(brand_car='Mazda')

    context = {
        'mazda': mazda
    }
    return render(request, 'mazda.html', context=context)


def car_bmw(request):

    bmw = Car.objects.filter(brand_car='Bmw')
    print(bmw)

    context = {
        'bmw': bmw
    }
    return render(request, 'bmw.html', context=context)


def car_audi(request):

    audi = Car.objects.filter(brand_car='Audi')

    context = {
        'audi': audi
    }
    return render(request, 'audi.html', context=context)
# Create your views here.
