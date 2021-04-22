import json
from .models import *


def cookiCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    items = []
    order = {'get_cart_total' :0 , 'get_cart_items' : 0}
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]["qunatity"]
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]["qunatity"])
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]["qunatity"]

            item = {
                'product':{
                    'id': product.id,
                    'name':product.name,
                    'price':product.price,
                    'imageURL':product.imageURL,

                },
                'qunatity':cart[i]["qunatity"],
                'get_total':total,
            }
            items.append(item)
        except:
            pass
    return {'cartItems' : cartItems , 'order' : order, 'items' : items}

def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookiData = cookiCart(request)
        cartItems = cookiData['cartItems']
        order = cookiData['order']
        items = cookiData['items']
    return {'cartItems' : cartItems , 'order' : order, 'items' : items}