from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def homepage(request):
    return redirect(to='tweet/')