# Generated by Django 5.0.7 on 2024-10-10 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0009_alter_profile_borrowed_books'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
