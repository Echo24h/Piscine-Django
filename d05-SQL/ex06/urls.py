from django.urls import path
from .views import init_view, populate_view, display_view, update_view

urlpatterns = [
    path('init/', init_view.init_view, name='init'),
    path('populate/', populate_view.populate_view, name='populate'),
    path('display/', display_view.display_view, name='display'),
    path('update/', update_view.update_view, name='update'),
]