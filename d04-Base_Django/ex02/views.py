from django.shortcuts import render
from django.conf import settings
from .forms import SubmissionForm
import os
from datetime import datetime

def handle_submission(text):
    # Chemin du fichier de log
    log_file_path = settings.LOG_FILE_PATH

    # Créer le dossier si nécessaire
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    # Écrire dans le fichier de log
    with open(log_file_path, 'a') as log_file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_file.write(f'{timestamp}: {text}\n')

def ex02_view(request):
    form = SubmissionForm()
    history = []

    # Charger l'historique depuis le fichier de log
    log_file_path = settings.LOG_FILE_PATH
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as log_file:
            history = log_file.readlines()

    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            handle_submission(text)
            # Ajouter la nouvelle entrée à l'historique
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            history.append(f'{timestamp}: {text}\n')

    return render(request, 'ex02/ex02.html', {
        'form': form,
        'history': history
    })