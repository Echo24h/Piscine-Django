from django.shortcuts import render
from django.http import HttpResponse

def generate_color_table():
    colors = ['black', 'red', 'blue', 'green']
    num_rows = 50
    color_steps = 255 // (num_rows - 1)  # Nous voulons 50 nuances, donc 49 étapes
    
    table_data = []

    for row in range(num_rows):
        row_data = []
        for color in colors:
            # Calculer l'intensité de la couleur pour chaque nuance
            intensity = row * color_steps
            
            if color == 'black':
                color_hex = f'#{intensity:02x}{intensity:02x}{intensity:02x}'  # Nuance de noir
            elif color == 'red':
                color_hex = f'#{intensity:02x}0000'  # Nuance de rouge
            elif color == 'blue':
                color_hex = f'#0000{intensity:02x}'  # Nuance de bleu
            elif color == 'green':
                color_hex = f'#00{intensity:02x}00'  # Nuance de vert

            row_data.append(color_hex)
        table_data.append(row_data)

    return table_data

def ex03_view(request):
    table_data = generate_color_table()
    return render(request, 'ex03/ex03.html', {'table_data': table_data})