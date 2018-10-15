from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse, Http404
import mongoengine

# Create your views here.

from Cours.models import *

user = authenticate(username=username, password=password)
assert isinstance(user, mongoengine.django.auth.User)

def index():
    try:
        # Création d'un utilisateur
        user = User(firstname="Erwann", lastname="Guillevic", email="erwann.guillevic@ynov.com", password="p@ssword")
        user.save()
        users = User.objects.all()
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render('user/user.html', {'users': users})
