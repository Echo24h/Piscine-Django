from django.urls import path
from .views.init_view import init_db
from .views.populate_view import populate_view
from .views.display_view import display_view
from .views.remove_view import remove_view

urlpatterns = [
    path('init/', init_db, name='init'),
    path('populate/', populate_view, name='populate'),
    path('display/', display_view, name='display'),
    path('remove/', remove_view, name='remove'),
]