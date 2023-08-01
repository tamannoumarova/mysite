from notebook.models import Notebook
from django import forms


class NotebookForm(forms.ModelForm):
    class Meta:
        model = Notebook
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "brand": forms.TextInput(attrs={"class": "form-control"}),
            "number": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            'group': forms.Select(attrs={'class': 'form-control'}),
        }