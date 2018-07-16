from django.shortcuts import render, HttpResponse, redirect
from apps.amadon_shop.models import *

def index(request):
    return render(request, 'amadon_shop/index.html', {'items': Item.objects.all()})

def purchase(request):
    product_id = int(request.POST['product_id'])
    quantity = int(request.POST['quantity'])
    item_bought = Item.objects.get(id=product_id)
    item_bought.item_count +=quantity
    item_bought.save()
    current_purchase = item_bought.item_price
    total_spent = 0
    total_items = 0

    for i in Item.objects.all():
        total_spent += (i.item_price * i.item_count)
        total_items = total_items + i.item_count
    
    request.session['current_purchase'] = float(current_purchase)
    request.session['total_spent'] = float(total_spent)
    request.session['total_items'] = total_items

    return redirect('/confirmation')

def confirmation(request):
    return render(request, 'amadon_shop/confirmation.html')
