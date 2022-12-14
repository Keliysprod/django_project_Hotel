from django.shortcuts import render
from django.shortcuts import redirect
from .models import Listings
from .forms import ListingsForm

def post_list(request):
    listings=Listings.objects.all()
    context={
        'listings':listings
    }
    return render(request, 'post_list.html', context)


def post_retrieve(request, pk):
    listing=Listings.objects.get(id=pk)
    context={
        'listing':listing
    }
    return render(request, 'post_retrieve.html', context)


def post_create(request):
    form=ListingsForm()
    if request.method == 'POST':
        form=ListingsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listings/')

    context={
        'form':form
    }
    return render(request, 'post_create.html',context)



def post_update(request,pk):
    listing=Listings.objects.get(id=pk)
    form=ListingsForm(instance=listing)
    if request.method == 'POST':
        form=ListingsForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('/listings/')

    context={
        'form':form
    }
    return render(request, 'post_create.html',context)


def post_delete(request, pk):
    listing=Listings.objects.get(id=pk)
    listing.delete()
    return redirect('/listings/')