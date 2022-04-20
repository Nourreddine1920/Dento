from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('blog-details.html', views.blog_details, name='blog-details'),
    path('blog.html', views.blog, name='blog'),
    path('index-2.html', views.index, name='index'),
    path('pricing.html', views.pricing, name='pricing'),
    path('service.html', views.service, name='service'),
    path('appointment.html', views.appointment, name='appointment'),
    path('about.html', views.about, name='about'),





]
