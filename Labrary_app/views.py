from django.shortcuts import render
from .models import BookCipher, RecommendedLiterature

def index(request):
    # Извлекаем все данные из таблиц
    book_ciphers = BookCipher.objects.all()
    recommended_literature = RecommendedLiterature.objects.all()
    # Передаем данные в шаблон
    return render(request, 'index.html', {
        'title': 'Library Catalog',
        'book_ciphers': book_ciphers,
        'recommended_literature': recommended_literature
    })