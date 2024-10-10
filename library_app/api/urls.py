from django.urls import path, include
from library_app.api.views import book_list, book_details, category_list, category_details, review_details, review_create, borrow_book, return_book

urlpatterns = [
    path('list/', book_list, name='book-list'),
    path('<int:pk>/', book_details, name='book-detail'),
    path('category/list/', category_list, name='category-list'),
    path('category/<int:pk>/', category_details, name='category-detail'),
    path('borrow_book/<int:pk>/', borrow_book, name='borrow-book'),
    path('return_book/<int:pk>/', return_book, name='return-book'),
    path('create-review/<int:pk>/', review_create, name='create-review'),
    path('review/<int:pk>/', review_details, name='review-detail')
]