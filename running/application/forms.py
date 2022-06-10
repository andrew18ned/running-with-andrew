from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields
from .models import Profile
from django.contrib.auth.forms import UserCreationForm



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email']