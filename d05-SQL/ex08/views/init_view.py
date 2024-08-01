from django.http import HttpResponse
from django.db import connection as conn

def init(request):

    with conn.cursor() as cursor:
        try:
            # Connexion à la base de données

            # Créer la table ex08_planets
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex08_planets (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                climate VARCHAR,
                diameter INTEGER,
                orbital_period INTEGER,
                population BIGINT,
                rotation_period INTEGER,
                surface_water REAL,
                terrain VARCHAR(128)
            );
            """)

            # Créer la table ex08_people
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex08_people (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                birth_year VARCHAR(32),
                gender VARCHAR(32),
                eye_color VARCHAR(32),
                hair_color VARCHAR(32),
                height INTEGER,
                mass REAL,
                homeworld VARCHAR(64),
                FOREIGN KEY (homeworld) REFERENCES ex08_planets(name)
            );
            """)

            conn.commit()
            cursor.close()
            conn.close()

            return HttpResponse("Tables created successfully.")
        except Exception as e:
            return HttpResponse(f"Error: {e}")