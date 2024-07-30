from django.urls import path
from . import views

urlpatterns = [
    path('', views.ex03_view, name='ex03'),
]