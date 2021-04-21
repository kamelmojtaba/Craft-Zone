from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
import json
from .models import *
import datetime

from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# remove this ==> @login_required <== if you don't want the index page to require login
@login_required
def index(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total' :0 , }
		cartItems = order['get_cart_items']


	products = Product.objects.all()
	context= {'products' :products, 'cartItems' : cartItems , }
	return render(request, 'index.html', context)

def contact(request):
	if request.method == "POST":
		Name = request.POST['Name']
		Email = request.POST['Email']
		Phone = request.POST['Phone']
		text3 = request.POST['text3']
		return render(request, 'contact.html', {'Name': Name})

	else:
		return render(request, 'contact.html', {})


def clients(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total' :0 , }
		cartItems = order['get_cart_items']


	products = Product.objects.all()
	context= {'products' :products, 'cartItems' : cartItems , }
	return render(request, 'clients.html', context)

def testmonial(request):
	return render(request, 'testmonial.html', {})

def about(request):
	return render(request, 'about.html', {})

def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		items = []
		order = {'get_cart_total' :0 , }
	context= {'items' :items, 'order' : order}
	return render(request, 'cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		items = []
		order = {'get_cart_total' :0 , }

	context= {'items' :items, 'order' : order}
	return render(request, 'checkout.html', context)



def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('action:', action)
	print('productId:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.qunatity = (orderItem.qunatity + 1)
	elif action == 'remove' :
		orderItem.qunatity = (orderItem.qunatity - 1)

	orderItem.save()

	if orderItem.qunatity <= 0 :
		orderItem.delete()
		
	
	return JsonResponse('Item was added', safe=False)

def processOrder(request):
		transaction_id = datetime.datetime.now().timestamp()
		data = json.loads(request.body)

		if request.user.is_authenticated:
			customer = request.user.customer
			order, created = Order.objects.get_or_create(customer=customer, complete=False)
			total = float(data['form']['total'])
			order.transaction_id = transaction_id

			if total == order.get_cart_total:
				order.complete = True 
			order.save()

			ShippingAddress.objects.create(
				customer=customer,
				order=order,
				country=data['shipping']['country'],
				address=data['shipping']['address'],
				city=data['shipping']['city'],
				state=data['shipping']['state'],
				phone_number=data['shipping']['phone_number'],
				)

		else :
			print('user is not logged in ')
		return JsonResponse('payment done', safe=False)

def login_page(request):
	return render(request, 'LogIn.html', {})

def signup(request):
	return render(request, 'signUp.html', {})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))

			else:
				return HttpResponse("Account not active! ")
		else:
			return HttpResponse("invalid login details!")
	else:
		return render(request, 'craftapp/login.html')

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))