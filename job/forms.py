from django import forms
from django.forms import fields
from .models import Apply


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email', 'website', 'cv', 'cover_letter']
