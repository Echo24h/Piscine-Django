from django.urls import path
from .views.init_view import init
from .views.populate_view import populate
from .views.display_view import display

urlpatterns = [
    path('init/', init, name='init'),
    path('populate/', populate, name='populate'),
    path('display/', display, name='display'),
]