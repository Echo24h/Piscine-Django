from django.urls import path
from .views import init_view, populate_view, display_view

urlpatterns = [
    path('init', init_view.init, name='init'),
    path('populate', populate_view.populate, name='populate'),
    path('display', display_view.display, name='display'),
]