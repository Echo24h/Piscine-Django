from django.shortcuts import render, redirect
from django.http import HttpResponse
from ex05.forms import MovieRemoveForm
from ex05.models import Movies

def remove_movie(request):

    if not Movies.objects.exists():
        return HttpResponse("No data available")
    
    if request.method == 'POST':
        form = MovieRemoveForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            Movies.objects.filter(title=title).delete()
            return redirect('ex05:remove')
    else:
        form = MovieRemoveForm()
    return render(request, 'remove.html', {'form': form})