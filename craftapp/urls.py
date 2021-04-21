from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'craftapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('contact.html', views.contact, name="contact"),
    path('clients.html', views.clients, name="clients"),
    path('testmonial.html', views.testmonial, name="testmonial"),
    path('about.html', views.about, name="about"),
    path('cart.html', views.cart, name="cart"),
    path('checkout.html', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('LogIn.html', views.login_page, name="LogIn"),
    url('user_login', views.user_login, name='user_login'),
    path('signUp.html', views.signup, name="signUp"),
]
