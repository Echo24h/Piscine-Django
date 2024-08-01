from django.db import connection
from django.http import HttpResponse

def init(request):
    try:
        with connection.cursor() as cursor:
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS ex02_movies (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb SERIAL PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            );
            '''
            cursor.execute(create_table_query)
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {e}")