from django.urls import path
from .views.populate_view import populate_db
from .views.display_view import display_db
from .views.remove_view import remove_movie

app_name = 'ex05'
urlpatterns = [
    path('populate/', populate_db, name='populate'),
    path('display/', display_db, name='display'),
    path('remove/', remove_movie, name='remove'),
]