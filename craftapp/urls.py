from django.urls import path
from django.contrib.auth import views as auth_views
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
    path('LogIn.html', auth_views.LoginView.as_view(template_name="LogIn.html"), name="login"),
    path('signUp.html', views.signup, name="signUp"),
    path('account', views.Account, name="Account"),
]
