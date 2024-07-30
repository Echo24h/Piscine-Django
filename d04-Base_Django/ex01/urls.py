from django.urls import path
from . import views

urlpatterns = [
    path('django/', views.django_view, name='django'),
    path('affichage/', views.affichage_view, name='affichage'),
    path('templates/', views.templates_view, name='templates'),
]