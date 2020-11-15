from django import forms
from django.forms import widgets
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'description', 'due_date']
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }