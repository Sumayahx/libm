# Generated by Django 5.0.7 on 2024-10-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0005_borrowed_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='amount_available',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
