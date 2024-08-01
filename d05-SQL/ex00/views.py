from django.http import HttpResponse
import psycopg2
from psycopg2 import sql

def init_db(request):
    try:
        # Connexion à la base de données
        conn = psycopg2.connect(
            dbname="formationdjango",
            user="djangouser",
            password="secret",
            host="localhost"
        )
        cur = conn.cursor()

        # Création de la table
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS ex00_movies (
            title VARCHAR(64) UNIQUE NOT NULL,
            episode_nb SERIAL PRIMARY KEY,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
        );
        '''
        cur.execute(create_table_query)

        # Validation et fermeture de la connexion
        conn.commit()
        cur.close()
        conn.close()

        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {e}")