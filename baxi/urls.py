from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('pricing/',views.pricing, name='pricing'),
    path('contact/',views.contact, name='contact'),
    path('privacy-policy/',views.privacy_policy, name='privacy_policy')
]
