from django.shortcuts import render
from django.conf import settings
import random
from django.utils import timezone

def get_random_username():
    return random.choice(settings.ANONYMOUS_USERNAMES)

def home(request):
    now = timezone.now()
    
    # Check if the session contains a username and its timestamp
    if 'anonymous_username' in request.session:
        username = request.session['anonymous_username']
        timestamp = request.session['username_timestamp']
        timestamp = timezone.datetime.fromisoformat(timestamp)
        
        # Check if the username has expired
        if (now - timestamp) > settings.ANONYMOUS_USER_TIMEOUT:
            username = get_random_username()
            request.session['anonymous_username'] = username
            request.session['username_timestamp'] = now.isoformat()
    else:
        username = get_random_username()
        request.session['anonymous_username'] = username
        request.session['username_timestamp'] = now.isoformat()

    return render(request, 'ex/home.html', {'username': username})