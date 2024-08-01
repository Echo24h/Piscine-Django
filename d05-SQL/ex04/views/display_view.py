from django.http import HttpResponse
from django.template import loader
from django.db import connection as conn

def display_view(request):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM ex04_movies")
            rows = cursor.fetchall()
        
        if not rows:
            return HttpResponse("No data available")
        
        template = loader.get_template('ex04/display.html')
        context = {'movies': rows}
        return HttpResponse(template.render(context, request))
    except Exception as e:
        return HttpResponse(f"Error displaying data: {str(e)}")