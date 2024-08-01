from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from ex04.forms import MovieRemoveForm

def remove_view(request):
    if request.method == 'POST':
        form = MovieRemoveForm(request.POST)
        if form.is_valid():
            title_to_remove = form.cleaned_data['title']
            try:
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM ex04_movies WHERE title = %s", [title_to_remove])
                    connection.commit()
                # Redirect to the same page to update the list
                return redirect('remove')
            except Exception as e:
                return HttpResponse(f"Error removing movie: {str(e)}")
    else:
        form = MovieRemoveForm()

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT title FROM ex04_movies")
            titles = cursor.fetchall()

        if not titles:
            return HttpResponse("No data available")
        
        # Update the form choices
        form.fields['title'].choices = [(title[0], title[0]) for title in titles]
        return render(request, 'ex04/remove.html', {'form': form})

    except Exception as e:
        return HttpResponse(f"Error fetching movie titles: {str(e)}")