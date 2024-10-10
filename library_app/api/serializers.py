from rest_framework import serializers
from library_app.models import Book, Review, Category
from library_app.models import Borrowed_book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"

    avg_rating = serializers.StringRelatedField(read_only=True)
    category = serializers.CharField(source='category.name')

class CategorySerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"

class BorrowSerializer(serializers.ModelSerializer):
    
        model = Borrowed_book
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"