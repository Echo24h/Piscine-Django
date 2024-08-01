from django.shortcuts import HttpResponse
from django.db import connection

def display_view(request):
    with connection.cursor() as cursor:
        try:
            cursor.execute('SELECT * FROM ex06_movies;')
            movies = cursor.fetchall()
            if not movies:
                return HttpResponse("No data available")
            
            response = "<table>"
            response += "<tr><th>Episode</th><th>Title</th><th>Openin Crawl</th><th>Director</th><th>Producer</th><th>Release Date</th><th>Created</th><th>Updated</th></tr>"
            for movie in movies:
                response += "<tr>"
                response += "".join([f"<td>{field}</td>" for field in movie])
                response += "</tr>"
            response += "</table>"
            
            return HttpResponse(response)
        except Exception as e:
            return HttpResponse(f"Error: {e}")