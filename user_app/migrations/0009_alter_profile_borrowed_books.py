# Generated by Django 5.0.7 on 2024-10-10 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0008_alter_book_amount_available'),
        ('user_app', '0008_remove_profile_borrowed_books_profile_borrowed_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='borrowed_books',
            field=models.ManyToManyField(blank=True, related_name='borrower', to='library_app.book'),
        ),
    ]
