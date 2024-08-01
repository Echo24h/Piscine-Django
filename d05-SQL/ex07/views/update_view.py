from django.shortcuts import render, redirect
from ex07.forms import MovieUpdateForm
from ex07.models import Movies
from django.http import HttpResponse

def update_view(request):
    movies = Movies.objects.all()
    if not movies:
        return HttpResponse("No data available")
    
    if request.method == 'POST':
        form = MovieUpdateForm(request.POST)
        form.fields['title'].choices = [(movie.title, movie.title) for movie in movies]

        if form.is_valid():
            title = form.cleaned_data['title']
            opening_crawl = form.cleaned_data['opening_crawl']
            # Mettre à jour l'instance correspondant au titre sélectionné
            Movies.objects.filter(title=title).update(opening_crawl=opening_crawl)
            return HttpResponse("OK")
    else:
        form = MovieUpdateForm()
        form.fields['title'].choices = [(movie.title, movie.title) for movie in movies]
    
    return render(request, 'ex07/update.html', {'form': form})