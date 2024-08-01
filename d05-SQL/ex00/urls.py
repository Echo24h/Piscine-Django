from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.init_db, name='init_db'),
]