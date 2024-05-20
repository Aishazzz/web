from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'description', 'cover_photo', 'status']
        widgets = {
            'status': forms.HiddenInput(),
        }