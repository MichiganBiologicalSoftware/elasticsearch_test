from uuid import uuid4
from random import randint

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from cars.models import Car
from cars.documents import CarDocument

def index(request):
    es_s = CarDocument.search().scan()
    
    context = {'cars': []}

    for car in es_s:
        datum = {}
        datum['id'] = car.id
        datum['created'] = car.created
        context['cars'].append(datum)
    
    context['cars'] = sorted(context['cars'], key=lambda datum: datum['created'], reverse=True)

    return render(request, 'index.html', context)

def make(request):
    colors = ["Red", "Blue", "Pink", "Magenta"]
    descriptions = ["Great car", "Awful car", "Ran over a hobo with it"]
    owner_names = ["Ali", "Tommy", "Dan", "Catherine"]

    car_type = [1,2,4][randint(a=0, b=2)]
    car_color = colors[randint(a=0, b=len(colors)-1)]
    car_desc = descriptions[randint(a=0, b=len(descriptions)-1)]
    owner_name = owner_names[randint(a=0, b = len(owner_names)-1)]

    car = Car(
        name= owner_name,
        color=car_color,
        type=car_type,
        description=car_desc,
        created =  timezone.now()
    )
    car.save()

    return redirect(to='index')

def view(request, car_id):
    this_car = None
    try:
        this_car = Car.objects.get(id=car_id)
    except Exception as exc:
        print(exc)
        return redirect(to='index')

    context = {}
    context['id'] = this_car.id
    context['owner_name'] = this_car.owner_name
    context['color'] = this_car.color
    context['type'] = this_car.get_type_display()
    context['description'] = this_car.description
    context['created'] = this_car.created

    return render(request, 'car.html', context)