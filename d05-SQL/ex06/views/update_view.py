from django.shortcuts import render, HttpResponse
from django.db import connection
from ex06.forms import MovieUpdateForm

def update_view(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT title FROM ex06_movies;')
        movies = cursor.fetchall()
        if not movies:
            return HttpResponse("No data available")
    
    if request.method == 'POST':
        form = MovieUpdateForm(request.POST)
        form.fields['title'].choices = [(movie[0], movie[0]) for movie in movies]  # Update choices dynamically

        if form.is_valid():
            title = form.cleaned_data['title']
            opening_crawl = form.cleaned_data['opening_crawl']
            
            with connection.cursor() as cursor:
                try:
                    cursor.execute('''
                        UPDATE ex06_movies 
                        SET opening_crawl = %s 
                        WHERE title = %s;
                    ''', [opening_crawl, title])
                    return HttpResponse("OK")
                except Exception as e:
                    return HttpResponse(f"Error: {e}")
    else:
        form = MovieUpdateForm()
        form.fields['title'].choices = [(movie[0], movie[0]) for movie in movies]  # Update choices dynamically
    
    return render(request, 'update.html', {'form': form})