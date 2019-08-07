from django.shortcuts import render, redirect
from .models import Nono

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    name = request.GET.get('name')
    category = request.GET.get('category')
    replace = request.GET.get('replace')

    nono = Nono()
    nono.name = name
    nono.category = category
    nono.replace = replace
    nono.save()

    # return render(request, 'create.html')
    return redirect('/product/')

def index(request):
    nonos = Nono.objects.all()
    context = {
        'nonos': nonos,
    }
    return render(request, 'index.html', context)

def detail(request, nono_id):
    nono = Nono.objects.get(id=nono_id)
    context = {
        'nono': nono,
    }
    return render(request, 'detail.html', context)

def delete(request, nono_id):
    nono = Nono.objects.get(id=nono_id)
    nono.delete()
    # return render(request, 'delete.html')
    return redirect('/product/')

def edit(request, nono_id):
    nono = Nono.objects.get(id=nono_id)
    context = {
        'nono': nono,
    }
    return render(request,'edit.html', context)

def update(request, nono_id):
    name = request.GET.get('name')
    category = request.GET.get('category')
    replace = request.GET.get('replace')

    nono = Nono.objects.get(id=nono_id)
    nono.name = name
    nono.category = category
    nono.replace = replace
    nono.save()

    # return render(request, 'update.html')
    return redirect(f'/product/{nono_id}/')