from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Movies

def populate(request):
    movies_data = [
        {'episode_nb': 1, 'title': 'The Phantom Menace', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '1999-05-19'},
        {'episode_nb': 2, 'title': 'Attack of the Clones', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '2002-05-16'},
        {'episode_nb': 3, 'title': 'Revenge of the Sith', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '2005-05-19'},
        {'episode_nb': 4, 'title': 'A New Hope', 'director': 'George Lucas', 'producer': 'Gary Kurtz, Rick McCallum', 'release_date': '1977-05-25'},
        {'episode_nb': 5, 'title': 'The Empire Strikes Back', 'director': 'Irvin Kershner', 'producer': 'Gary Kutz, Rick McCallum', 'release_date': '1980-05-17'},
        {'episode_nb': 6, 'title': 'Return of the Jedi', 'director': 'Richard Marquand', 'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum', 'release_date': '1983-05-25'},
        {'episode_nb': 7, 'title': 'The Force Awakens', 'director': 'J. J. Abrams', 'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', 'release_date': '2015-12-11'}
    ]

    responses = []
    for data in movies_data:
        try:
            movie, created = Movies.objects.update_or_create(
                episode_nb=data['episode_nb'],
                defaults={
                    'title': data['title'],
                    'director': data['director'],
                    'producer': data['producer'],
                    'release_date': data['release_date']
                }
            )
            if created:
                responses.append(f"OK: {data['title']}")
            else:
                responses.append(f"Already exists: {data['title']}")
        except Exception as e:
            responses.append(f"Error inserting {data['title']}: {e}")

    return HttpResponse("<br>".join(responses))


def display(request):
    movies = Movies.objects.all()

    if not movies:
        return HttpResponse("No data available")

    html = "<table border='1'>"
    html += "<tr><th>Episode Number</th><th>Title</th><th>Opening Crawl</th><th>Director</th><th>Producer</th><th>Release Date</th></tr>"
    for movie in movies:
        html += "<tr>"
        html += f"<td>{movie.episode_nb}</td>"
        html += f"<td>{movie.title}</td>"
        html += f"<td>{movie.opening_crawl or ''}</td>"
        html += f"<td>{movie.director}</td>"
        html += f"<td>{movie.producer}</td>"
        html += f"<td>{movie.release_date}</td>"
        html += "</tr>"
    html += "</table>"

    return HttpResponse(html)