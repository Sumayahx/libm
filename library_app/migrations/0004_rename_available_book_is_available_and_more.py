# Generated by Django 5.0.7 on 2024-09-30 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0003_book_number_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='available',
            new_name='is_available',
        ),
        migrations.RemoveField(
            model_name='book',
            name='created',
        ),
        migrations.AddField(
            model_name='book',
            name='amount_available',
            field=models.IntegerField(default=0),
        ),
    ]
