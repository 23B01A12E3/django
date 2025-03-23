from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def item_list(request):
    items = Item.objects.all()
    return render(request, 'dbapp/item.html', {'items': items})

def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item')
    else:
        form = ItemForm()
    return render(request, 'dbapp/add_item.html', {'form': form})
