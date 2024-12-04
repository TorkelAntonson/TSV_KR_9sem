from django.db import models
from Labrary_app.models import RecommendedLiterature, BookCipher

rec_lit_data = [
    {
        'discipline_name': 'Психология',
        'author_last_name': 'Пиажет',
        'book_title': 'Психология интеллекта'
    },
    {
        'discipline_name': 'Философия',
        'author_last_name': 'Платон',
        'book_title': 'Государство'
    },
    {
        'discipline_name': 'Социология',
        'author_last_name': 'Дюркгейм',
        'book_title': 'Правила социологического метода'
    },
    {
        'discipline_name': 'Литература',
        'author_last_name': 'Толстой',
        'book_title': 'Война и мир'
    },
    {
        'discipline_name': 'История',
        'author_last_name': 'Гиббон',
        'book_title': 'История упадка и разрушения Римской империи'
    },
    {
        'discipline_name': 'Физика',
        'author_last_name': 'Ньютон',
        'book_title': 'Математические начала натуральной философии'
    },
    {
        'discipline_name': 'Экономика',
        'author_last_name': 'Смит',
        'book_title': 'Исследование о природе и причинах богатства народов'
    },
    {
        'discipline_name': 'Математика',
        'author_last_name': 'Коши',
        'book_title': 'Курс анализа'
    },
    {
        'discipline_name': 'Логика',
        'author_last_name': 'Арнольд',
        'book_title': 'Логика и теоретическая философия'
    },
    {
        'discipline_name': 'Физика',
        'author_last_name': 'Эйнштейн',
        'book_title': 'Общие задачи теории относительности'
    },
    {
        'discipline_name': 'Психология',
        'author_last_name': 'Фрейд',
        'book_title': 'Толкование сновидений'
    },
    {
        'discipline_name': 'Медицина',
        'author_last_name': 'Гиппократ',
        'book_title': 'Собрание произведений'
    },
    {
        'discipline_name': 'Химия',
        'author_last_name': 'Менделеев',
        'book_title': 'Основы химии'
    },
    {
        'discipline_name': 'Культурология',
        'author_last_name': 'Шпенглер',
        'book_title': 'Закат Европы'
    },
    {
        'discipline_name': 'Литература',
        'author_last_name': 'Достоевский',
        'book_title': 'Преступление и наказание'
    },
    {
        'discipline_name': 'Биология',
        'author_last_name': 'Дарвин',
        'book_title': 'Происхождение видов'
    },
    {
        'discipline_name': 'Социология',
        'author_last_name': 'Вебер',
        'book_title': 'Протестантская этика и дух капитализма'
    },
    {
        'discipline_name': 'Математика',
        'author_last_name': 'Гаусс',
        'book_title': 'Диссертация о числах'
    },
    {
        'discipline_name': 'Философия',
        'author_last_name': 'Ницше',
        'book_title': 'Так говорил Заратустра'
    },
    {
        'discipline_name': 'Политология',
        'author_last_name': 'Макиавелли',
        'book_title': 'Государь'
    }
]    
def bulk_create_RecommendedLiterature():
# Создаем список объектов модели
    rec_lit = [
    RecommendedLiterature(
        discipline_name = data['discipline_name'],
        author_last_name = data['author_last_name'],
        book_title = data['book_title']
    )
    for data in rec_lit_data
    ]
    # Используйте bulk_create для добавления всех записей
    RecommendedLiterature.objects.bulk_create(rec_lit)


book_cp_data = [
    {
        'author_last_name': 'Пиажет',
        'book_title': 'Психология интеллекта',
        'library_cipher': 'PSY-001.01'
    },
    {
        'author_last_name': 'Платон',
        'book_title': 'Государство',
        'library_cipher': 'PHI-001.02'
    },
    {
        'author_last_name': 'Дюркгейм',
        'book_title': 'Правила социологического метода',
        'library_cipher': 'SOC-002.01'
    },
    {
        'author_last_name': 'Толстой',
        'book_title': 'Война и мир',
        'library_cipher': 'LIT-003.01'
    },
    {
        'author_last_name': 'Гиббон',
        'book_title': 'История упадка и разрушения Римской империи',
        'library_cipher': 'HIS-004.01'
    },
    {
        'author_last_name': 'Ньютон',
        'book_title': 'Математические начала натуральной философии',
        'library_cipher': 'PHY-005.01'
    },
    {
        'author_last_name': 'Смит',
        'book_title': 'Исследование о природе и причинах богатства народов',
        'library_cipher': 'ECO-006.01'
    },
    {
        'author_last_name': 'Коши',
        'book_title': 'Курс анализа',
        'library_cipher': 'MAT-007.01'
    },
    {
        'author_last_name': 'Арнольд',
        'book_title': 'Логика и теоретическая философия',
        'library_cipher': 'LOG-008.01'
    },
    {
        'author_last_name': 'Эйнштейн',
        'book_title': 'Общие задачи теории относительности',
        'library_cipher': 'PHY-009.01'
    },
    {
        'author_last_name': 'Фрейд',
        'book_title': 'Толкование сновидений',
        'library_cipher': 'PSY-010.01'
    },
    {
        'author_last_name': 'Гиппократ',
        'book_title': 'Собрание произведений',
        'library_cipher': 'MED-011.01'
    },
    {
        'author_last_name': 'Менделеев',
        'book_title': 'Основы химии',
        'library_cipher': 'CHE-012.01'
    },
    {
        'author_last_name': 'Шпенглер',
        'book_title': 'Закат Европы',
        'library_cipher': 'CUL-013.01'
    },
    {
        'author_last_name': 'Достоевский',
        'book_title': 'Преступление и наказание',
        'library_cipher': 'LIT-014.01'
    },
    {
        'author_last_name': 'Дарвин',
        'book_title': 'Происхождение видов',
        'library_cipher': 'BIO-015.01'
    },
    {
        'author_last_name': 'Вебер',
        'book_title': 'Протестантская этика и дух капитализма',
        'library_cipher': 'SOC-016.01'
    },
    {
        'author_last_name': 'Гаусс',
        'book_title': 'Диссертация о числах',
        'library_cipher': 'MAT-017.01'
    },
    {
        'author_last_name': 'Ницше',
        'book_title': 'Так говорил Заратустра',
        'library_cipher': 'PHI-018.01'
    },
    {
        'author_last_name': 'Макиавелли',
        'book_title': 'Государь',
        'library_cipher': 'POL-019.01'
    }
]

def bulk_create_BookCipher():
# Создаем список объектов модели
    book_cp = [
    BookCipher(
        author_last_name = data_1['author_last_name'],
        book_title = data_1['book_title'],
        library_cipher = data_1['library_cipher']
    )
    for data_1 in book_cp_data
    ]
    # Используйте bulk_create для добавления всех записей
    BookCipher.objects.bulk_create(book_cp)
