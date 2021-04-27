from django.shortcuts import render
from django.http.response import JsonResponse
from basket.basket import Basket
from .models import Order,OrderItem


def add(request):
    basket=Basket(request)
    if request.POST.get('action') == 'post':

        user_id = request.user.id
        order_key = request.POST.get('order_key')
        baskettotal = basket.get_total_price()
        name = request.POST.get('name')
        address1 = request.POST.get('line1')
        address2 = request.POST.get('line2')
        post_code = request.POST.get('postCode')


        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(user_id=user_id,name=name,address1=address1,
            address2=address2,post_code=post_code,total_paid=baskettotal,order_key=order_key)

            order_id=order.pk

            for item in basket:
                OrderItem.objects.create(order_id=order_id,product=item['product'],price=item['price'],quantity=item['qty'])
            
            response = JsonResponse ({'success':'Order Placed'})
            return response

def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)

def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders
