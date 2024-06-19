from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        exclude = ["id", "created_date"]

        labels = {
            "name": "Name",
            "description": "Description",
        }

        widgets = {
            "name": forms.TextInput(attrs={}),
            "description": forms.TextInput(attrs={}),
        }
