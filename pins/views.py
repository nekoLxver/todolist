from django.shortcuts import render, redirect
from django.http import HttpResponse
from pins.models import Pins

# Create your views here.


def index(request):
    if request.method == "POST":
        new_pin = Pins(text=request.POST['text'], author=request.POST['author'])
        new_pin.save()
    all_objs = Pins.objects.all()
    context = {
        "objs": all_objs
    }
    return render(request, "pins/index.html", context)


def change(request, id):
    if request.method == "POST":
        changed_pin = Pins.objects.get(id=id)
        changed_pin.text = request.POST['text']
        changed_pin.author = request.POST['author']
        changed_pin.save()
        return redirect('pins:index')
    context = {
        "id": id
    }
    return render(request, 'pins/change.html', context)


def delete(request, id):
    if request.method == "POST":
        changed_pin = Pins.objects.get(id=id)
        changed_pin.delete()
        return redirect('pins:index')
    context = {
        "id": id
    }
    return render(request, 'pins/delete.html', context)