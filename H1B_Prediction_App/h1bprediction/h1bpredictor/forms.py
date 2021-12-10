from django import forms
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PredictionsForm(forms.ModelForm):
    class Meta:
        model = Predictions
        fields='__all__'