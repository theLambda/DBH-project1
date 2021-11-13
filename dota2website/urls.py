"""Defines URL patterns for dota2website"""

from django.urls import path

from . import views

app_name = 'dota2website'
urlpatterns = [
    # home page
    path('', views.index, name='index')
]