from django.shortcuts import render
from .models import People
from django.http import HttpResponse

def display(request):
    people = People.objects.filter(homeworld__climate__icontains='windy').order_by('name')
    
    if not people:
        return HttpResponse("No data available, please use the following command line before use: 'python manage.py loaddata ex09_initial_data.json'")

    return render(request, 'ex09/display.html', {'people': people})