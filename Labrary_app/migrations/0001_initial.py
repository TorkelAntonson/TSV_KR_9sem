# Generated by Django 5.1 on 2024-11-13 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookCipher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_last_name', models.CharField(max_length=255)),
                ('book_title', models.CharField(max_length=255)),
                ('library_cipher', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RecommendedLiterature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline_name', models.CharField(max_length=255)),
                ('author_last_name', models.CharField(max_length=255)),
                ('book_title', models.CharField(max_length=255)),
            ],
        ),
    ]