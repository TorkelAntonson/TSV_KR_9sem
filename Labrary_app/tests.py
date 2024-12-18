from django.test import TestCase, Client
from django.urls import reverse
from .models import RecommendedLiterature, BookCipher
from .forms import RecommendedLiteratureForm, BookCipherForm

class IndexViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')  # Убедитесь, что маршрут совпадает с именем URL
        self.recommended_literature_data = {
            'author_last_name': 'Smith',
            'book_title': 'Django for Beginners',
            'discipline_name': 'Programming',
        }
        self.book_cipher_data = {
            'author_last_name': 'Smith',
            'book_title': 'Django for Beginners',
            'library_cipher': '1234',
        }

    def test_get_index(self):
        """Тест получения страницы index"""
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn('recommended_literature_form', response.context)
        self.assertIn('book_cipher_form', response.context)

    def test_post_add_recommended_literature(self):
        """Тест добавления записи в RecommendedLiterature"""
        post_data = {
            'add_recommended_literature': True,
            **self.recommended_literature_data
        }
        response = self.client.post(self.index_url, post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(RecommendedLiterature.objects.filter(book_title='Django for Beginners').exists())

    def test_post_add_book_cipher(self):
        """Тест добавления записи в BookCipher"""
        post_data = {
            'add_book_cipher': True,
            **self.book_cipher_data
        }
        response = self.client.post(self.index_url, post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(BookCipher.objects.filter(library_cipher='1234').exists())

    def test_post_delete_recommended_literature(self):
        """Тест удаления записи из RecommendedLiterature"""
        literature = RecommendedLiterature.objects.create(**self.recommended_literature_data)
        post_data = {
            'delete_recommended_literature': True,
            'delete_id': literature.id,
        }
        response = self.client.post(self.index_url, post_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(RecommendedLiterature.objects.filter(id=literature.id).exists())

    def test_post_delete_book_cipher(self):
        """Тест удаления записи из BookCipher"""
        cipher = BookCipher.objects.create(**self.book_cipher_data)
        post_data = {
            'delete_book_cipher': True,
            'delete_id': cipher.id,
        }
        response = self.client.post(self.index_url, post_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(BookCipher.objects.filter(id=cipher.id).exists())

    def test_grouped_data_in_context(self):
        """Тест корректности группировки данных в контексте"""
        RecommendedLiterature.objects.create(**self.recommended_literature_data)
        BookCipher.objects.create(**self.book_cipher_data)
        response = self.client.get(self.index_url)
        grouped_recommended_literature = response.context['grouped_recommended_literature']
        grouped_book_ciphers = response.context['grouped_book_ciphers']
        
        self.assertIn('Smith', grouped_recommended_literature)
        self.assertEqual(len(grouped_recommended_literature['Smith']), 1)
        self.assertIn('Smith', grouped_book_ciphers)
        self.assertEqual(len(grouped_book_ciphers['Smith']), 1)

    def test_merged_data_in_context(self):
        """Тест наличия объединенных данных в контексте"""
        RecommendedLiterature.objects.create(**self.recommended_literature_data)
        BookCipher.objects.create(**self.book_cipher_data)
        response = self.client.get(self.index_url)
        merged_data = list(response.context['merged_data'])
        
        self.assertGreater(len(merged_data), 0)
        self.assertIn('library_cipher', merged_data[0])
