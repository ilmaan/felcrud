from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Library

class Book_Registration(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['bname','bauthor','bquantity']
        widgets = {
            'bname': forms.TextInput(attrs={'class':'form-control'}),
            'bauthor': forms.TextInput(attrs={'class':'form-control'}),
            'bquantity': forms.TextInput(attrs={'class':'form-control'}),
        }