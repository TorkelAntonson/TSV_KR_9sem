# forms.py
from django import forms
from .models import RecommendedLiterature, BookCipher

class RecommendedLiteratureForm(forms.ModelForm):
    class Meta:
        model = RecommendedLiterature
        fields = ['discipline_name', 'author_last_name', 'book_title']

class BookCipherForm(forms.ModelForm):
    class Meta:
        model = BookCipher
        fields = ['author_last_name', 'book_title', 'library_cipher']
