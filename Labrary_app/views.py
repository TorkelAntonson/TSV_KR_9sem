# views.py
from django.shortcuts import render, redirect
from .models import RecommendedLiterature, BookCipher
from .forms import RecommendedLiteratureForm, BookCipherForm
from django.db import connection

def index(request):
    if request.method == 'POST':
        if 'add_recommended_literature' in request.POST:
            form = RecommendedLiteratureForm(request.POST)
            if form.is_valid():
                form.save()
        elif 'add_book_cipher' in request.POST:
            form = BookCipherForm(request.POST)
            if form.is_valid():
                form.save()
        elif 'delete_recommended_literature' in request.POST:
            id_to_delete = request.POST.get('delete_id')
            RecommendedLiterature.objects.filter(id=id_to_delete).delete()
        elif 'delete_book_cipher' in request.POST:
            id_to_delete = request.POST.get('delete_id')
            BookCipher.objects.filter(id=id_to_delete).delete()

    # Получаем данные из обеих таблиц
    recommended_literature = RecommendedLiterature.objects.all()
    book_ciphers = BookCipher.objects.all()

    # Группируем книги по автору для более понятного вывода
    grouped_recommended_literature = {}
    for record in recommended_literature:
        if record.author_last_name not in grouped_recommended_literature:
            grouped_recommended_literature[record.author_last_name] = []
        grouped_recommended_literature[record.author_last_name].append(record)

    grouped_book_ciphers = {}
    for record in book_ciphers:
        if record.author_last_name not in grouped_book_ciphers:
            grouped_book_ciphers[record.author_last_name] = []
        grouped_book_ciphers[record.author_last_name].append(record)
    
    #Склейка таблиц
    from django.db.models import OuterRef, Subquery, Value
    from django.db.models.functions import Coalesce

    # Используем Subquery для выборки library_cipher из модели BookCipher
    book_cipher_subquery = BookCipher.objects.filter(
        author_last_name=OuterRef('author_last_name'),
        book_title=OuterRef('book_title')
    ).values('library_cipher')[:1]

    # Объединяем данные из RecommendedLiterature и добавляем данные из BookCipher
    merged_data = RecommendedLiterature.objects.annotate(
        library_cipher=Coalesce(Subquery(book_cipher_subquery), Value("—"))
    ).values(
        'author_last_name', 'book_title', 'discipline_name', 'library_cipher'
    )

    # Объединяем все данные из BookCipher, где нет связей в RecommendedLiterature
    additional_data = BookCipher.objects.exclude(
        author_last_name__in=RecommendedLiterature.objects.values('author_last_name'),
        book_title__in=RecommendedLiterature.objects.values('book_title')
    ).annotate(
        discipline_name=Value("—")
    ).values(
        'author_last_name', 'book_title', 'discipline_name', 'library_cipher'
    )

    # Собираем все данные в один список
    merged_data_list = list(merged_data) + list(additional_data)

    # Отправляем все данные в шаблон
    context = {
        'recommended_literature': recommended_literature,
        'book_ciphers': book_ciphers,
        'grouped_recommended_literature': grouped_recommended_literature,
        'grouped_book_ciphers': grouped_book_ciphers,
        'recommended_literature_form': RecommendedLiteratureForm(),
        'book_cipher_form': BookCipherForm(),
        'merged_data': merged_data,
    }

    return render(request, 'index.html', context)
