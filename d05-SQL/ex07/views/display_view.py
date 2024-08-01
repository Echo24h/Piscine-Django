from django.shortcuts import render
from ex07.models import Movies
from django.http import HttpResponse

def display(request):
    movies = Movies.objects.all()
    if not movies:
        return HttpResponse("No data available")
    return render(request, 'ex07/display.html', {'movies': movies})