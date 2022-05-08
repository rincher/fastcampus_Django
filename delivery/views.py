from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from order.models import Order
# Create your views here.
@csrf_exempt
def order_list(request):
    if request.method == 'GET':
        order_list = Order.objects.all()
        return render(request, 'delivery/order_list.html', {'order_list' : order_list})
    
    elif request.method == 'POST':
        order_item = Order.objects.get(pk = int(request.POST['order_id']))
        order_item.deliver_finish = True
        order_item.save()
        return render(request, 'delivery/success.html')