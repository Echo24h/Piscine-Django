from django.http import HttpResponse
from django.db import connection as conn

def populate_view(request):
    data = [
        (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
        (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
        (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
        (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
        (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kutz, Rick McCallum', '1980-05-17'),
        (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
        (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11')
    ]

    try:
        with conn.cursor() as cursor:
            # Clear existing data
            cursor.execute("DELETE FROM ex04_movies")

            # Insert data
            for episode_nb, title, director, producer, release_date in data:
                cursor.execute("""
                    INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
                    VALUES (%s, %s, %s, %s, %s)
                """, (episode_nb, title, director, producer, release_date))
                conn.commit()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error inserting data: {str(e)}")