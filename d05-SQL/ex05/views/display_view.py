from django.http import HttpResponse
from django.shortcuts import render
from ex05.models import Movies

def display_db(request):
    movies = Movies.objects.all()
    if movies.exists():
        return render(request, 'display.html', {'movies': movies})
    else:
        return HttpResponse("No data available")