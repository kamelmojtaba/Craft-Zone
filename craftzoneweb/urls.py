from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from craftapp import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('craftapp.urls')),
    path('index.html', views.index, name="index" ),
    path('contact.html', views.contact, name="contact"),
    path('clients.html', views.clients, name="clients"),
    path('testmonial.html', views.testmonial, name="testmonial"),
    path('about.html', views.about, name="about"),
    path('cart.html', views.cart, name="cart"),
    path('checkout.html', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('signUp.html', views.signup, name="signUp"),
    url('logout/', views.user_logout, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
