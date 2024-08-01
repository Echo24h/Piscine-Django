from django.urls import path
from .views import populate_view, display_view, update_view

urlpatterns = [
    path('populate', populate_view.populate, name='populate'),
    path('display', display_view.display, name='display'),
    path('update', update_view.update_view, name='update'),
]