from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter todo title"}),
            "description": forms.Textarea(attrs={"rows": 3, "placeholder": "Optional description"}),
        }