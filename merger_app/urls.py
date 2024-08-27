# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('merger_app/', views.merger_app, name='merger_app'),
]