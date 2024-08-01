from django.shortcuts import HttpResponse
from django.db import connection

def init_view(request):
    with connection.cursor() as cursor:
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ex06_movies (
                    episode_nb SERIAL PRIMARY KEY,
                    title VARCHAR(64) UNIQUE NOT NULL,
                    opening_crawl TEXT,
                    director VARCHAR(32) NOT NULL,
                    producer VARCHAR(128) NOT NULL,
                    release_date DATE NOT NULL,
                    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            ''')
            cursor.execute('''
                CREATE OR REPLACE FUNCTION update_changetimestamp_column()
                RETURNS TRIGGER AS $$
                BEGIN
                    NEW.updated = now();
                    NEW.created = OLD.created;
                    RETURN NEW;
                END;
                $$ language 'plpgsql';
            ''')
            cursor.execute('''
                CREATE TRIGGER update_films_changetimestamp 
                BEFORE UPDATE ON ex06_movies 
                FOR EACH ROW EXECUTE PROCEDURE update_changetimestamp_column();
            ''')
            return HttpResponse("OK")
        except Exception as e:
            return HttpResponse(f"Error: {e}")