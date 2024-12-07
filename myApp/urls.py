from django.contrib import admin
from django.urls import path
from myApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('properties/', views.properties, name='properties'),
    path('services/', views.services, name='services'),
    path('starter/', views.starter, name='starter'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),

    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
]
