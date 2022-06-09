from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def auth(request):
    return render(request, 'auth.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


@login_required
def profile(request):
    # users_list = Account.objects.all()

    return render(request, 'profile.html')
