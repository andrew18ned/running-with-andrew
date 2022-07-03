from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from application.models import Runner


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
    name = request.user.username
    runer_list = Runner.objects.filter(runer_name=name)

    return render(request, 'profile.html', {'runer_list':runer_list})


def logout(request):
    return render(request, 'logout.html')