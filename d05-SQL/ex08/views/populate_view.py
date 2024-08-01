from django.http import HttpResponse
from django.db import connection as conn
import os
from django.conf import settings

def populate(request):
    with conn.cursor() as cursor:
        try:

            file_dir = os.path.join(settings.BASE_DIR, 'ex08/')

            cursor = conn.cursor()

            # Peupler la table ex08_planets
            with open(file_dir + 'planets.csv', 'r') as file:
                cursor.copy_from(file, 'ex08_planets', sep='\t', null='NULL', columns=(
                'name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain'
            ))

            # Peupler la table ex08_people
            with open(file_dir + 'people.csv', 'r') as file:
                cursor.copy_from(file, 'ex08_people', sep='\t', null='NULL', columns=(
                'name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld'
            ))
            
            conn.commit()
            cursor.close()
            conn.close()

            return HttpResponse("Data imported successfully.")
        except Exception as e:
            return HttpResponse(f"Error: {e}")