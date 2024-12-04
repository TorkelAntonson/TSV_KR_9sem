from django.db import models

class RecommendedLiterature(models.Model):
    discipline_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    book_title = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.discipline_name} - {self.author_last_name} - {self.book_title}'

class BookCipher(models.Model):
    author_last_name = models.CharField(max_length=255)
    book_title = models.CharField(max_length=255)
    library_cipher = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.author_last_name} - {self.book_title} - {self.library_cipher}'
