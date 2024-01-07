from django import forms
from .models import Workers

class WorkersForm(forms.ModelForm):
    class Meta:
        model = Workers
        fields = ['name', 'position', 'email', 'employment_date', 'parent']