from django.db import connection
from django.http import HttpResponse

def display(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM ex02_movies")
            rows = cursor.fetchall()

        if not rows:
            return HttpResponse("No data available")

        # Generate HTML table
        html = "<table border='1'>"
        html += "<tr><th>Episode Number</th><th>Title</th><th>Opening Crawl</th><th>Director</th><th>Producer</th><th>Release Date</th></tr>"
        for row in rows:
            html += "<tr>"
            for col in row:
                html += f"<td>{col}</td>"
            html += "</tr>"
        html += "</table>"

        return HttpResponse(html)
    except Exception as e:
        return HttpResponse(f"Error: {e}")