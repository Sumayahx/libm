from django.contrib import admin
from library_app.models import Book, Review, Category, Borrowed_book

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Borrowed_book)