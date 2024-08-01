from django.shortcuts import render
from django.db.models import Q
from .models import Movies, People, Planets
from .forms import SearchForm

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            min_release_date = form.cleaned_data['min_release_date']
            max_release_date = form.cleaned_data['max_release_date']
            min_planet_diameter = form.cleaned_data['min_planet_diameter']
            character_gender = form.cleaned_data['character_gender']
            
            # Query the database
            results = People.objects.filter(
                gender=character_gender,
                movies__release_date__range=[min_release_date, max_release_date],
                homeworld__diameter__gte=min_planet_diameter
            ).distinct().select_related('homeworld').prefetch_related('movies')
            
            if results:
                context = {
                    'results': results,
                    'min_release_date': min_release_date,
                    'max_release_date': max_release_date,
                    'min_planet_diameter': min_planet_diameter,
                    'character_gender': character_gender
                }
                return render(request, 'ex10/results.html', context)
            else:
                return render(request, 'ex10/search.html', {'form': form, 'message': 'Nothing corresponding to your research'})
    else:
        form = SearchForm()
    
    return render(request, 'ex10/search.html', {'form': form})