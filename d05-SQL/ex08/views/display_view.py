from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection as conn


def display(request):
    with conn.cursor() as cursor:
        try:
            cursor = conn.cursor()

            # Requête SQL pour obtenir les personnages et les détails de leur planète
            query = """
            SELECT p.name AS person_name, pl.name AS planet_name, pl.climate
            FROM ex08_people p
            JOIN ex08_planets pl ON p.homeworld = pl.name
            WHERE pl.climate ILIKE '%windy%'
            ORDER BY p.name;
            """
            cursor.execute(query)
            results = cursor.fetchall()

            cursor.close()
            conn.close()

            # Si aucun résultat n'est trouvé
            if not results:
                return HttpResponse("No data available")

            # Rendu du template avec les résultats
            return render(request, 'ex08/display.html', {'results': results})

        except Exception as e:
            return HttpResponse(f"Error: {e}")