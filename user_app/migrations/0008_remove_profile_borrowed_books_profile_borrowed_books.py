# Generated by Django 5.0.7 on 2024-10-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0008_alter_book_amount_available'),
        ('user_app', '0007_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='borrowed_books',
        ),
        migrations.AddField(
            model_name='profile',
            name='borrowed_books',
            field=models.ManyToManyField(to='library_app.book'),
        ),
    ]
