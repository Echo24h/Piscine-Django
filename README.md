# Piscine-Django

## Travailler dans un environnement virtuel Python

Create a virtual environment named django_venv

```bash
# Create a virtual environment named django_venv
python3 -m venv django_venv

# Activate the virtual environment
source django_venv/bin/activate

# Install the requirements
pip install -r requirement.txt

# Deactivate the virtual environment
deactivate
```

## Tutoriel d'utilisation Django

### Étape 1 : Installer Django

Utilisez le fichier requirement.txt pour l'installation

```bash
pip install -r requirement.txt
```

### Étape 2 : Créer un projet Django

Créez un nouveau projet Django en utilisant la commande suivante :

```bash
django-admin startproject myproject
```

### Étape 3 : Créer une application Django

Naviguez dans le répertoire du projet et créez une nouvelle application appelée helloworld :

```bash
cd myproject
python manage.py startapp helloworld
```

### Étape 4 : Configurer l'application

Ouvrez `myproject/settings.py` et ajoutez `helloworld` à la liste `INSTALLED_APPS` :

```python
INSTALLED_APPS = [
    ...
    'helloworld',
]
```

Ouvrez `helloworld/views.py` et ajoutez la fonction de vue suivante :

```python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World!")
```

Créez un fichier `urls.py` dans le répertoire `helloworld` et ajoutez le contenu suivant :

```python
from django.urls import path
from .views import hello_world

urlpatterns = [
    path('helloworld/', hello_world, name='hello_world'),
]
```

Ensuite, incluez ces URLs dans les URLs globales du projet. Ouvrez `myproject/urls.py` et modifiez-le comme suit :

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('helloworld.urls')),
]
```

### Étape 5 : Démarrer le serveur de développement

Exécutez les commandes suivantes pour démarrer le serveur de développement Django :

```bash
python manage.py migrate
python manage.py runserver
```

### Étape 6 : Vérifier le résultat

Ouvrez votre navigateur et allez à l'adresse `http://localhost:8000/helloworld`. Vous devriez voir la page afficher "Hello World!".