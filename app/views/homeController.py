# homeController.py deals with the default website redirection.

from django.shortcuts import redirect
from .userController import login
import urllib

# redirects user to feed if they are already logged in, otherwise sends to login
def home(request):
    # Equivalent of HomeController.java
    if request.session.get('username'):
        # BAD CODE:
        redir = urllib.request.Request('http://' + request.META['HTTP_HOST'] + '/feed')
        urllib.request.urlopen(redir)
        # GOOD CODE:
        # return redirect('feed')
    
    return login(request)