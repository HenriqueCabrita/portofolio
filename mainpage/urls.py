from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_me/', views.contact, name='contact'),
    path('about_me/', views.about, name='about'),
]