from django.db import connection
from django.http import HttpResponse

def populate(request):
    movies = [
        (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
        (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
        (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
        (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
        (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kutz, Rick McCallum', '1980-05-17'),
        (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
        (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11')
    ]
    
    response = []
    
    try:
        with connection.cursor() as cursor:
            for movie in movies:
                try:
                    insert_query = '''
                    INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
                    VALUES (%s, %s, %s, %s, %s);
                    '''
                    cursor.execute(insert_query, movie)
                    response.append(f"OK: {movie[1]}")
                except Exception as e:
                    response.append(f"Error inserting {movie[1]}: {e}")
        return HttpResponse("<br>".join(response))
    except Exception as e:
        return HttpResponse(f"Error: {e}")