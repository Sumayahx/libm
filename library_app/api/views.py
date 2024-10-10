from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from library_app.models import Book, Review, Category, Borrowed_book
from library_app.api.serializers import BookSerializer, BorrowSerializer, ReviewSerializer, CategorySerializer
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
@api_view(['GET', 'PUT', 'DELETE'])
def book_details(request, pk):
    if request.method == 'GET':
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'Error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    if request.method == 'PUT':
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
@api_view(['GET', 'PUT', 'DELETE'])
def category_details(request, pk):
    if request.method == 'GET':
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'Error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    if request.method == 'PUT':
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def borrow_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        if not book.is_available or book.amount_available == 0:
            return Response({'Book is currently not available. Please check again later.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            borrow = Borrowed_book.objects.create(user=request.user, book=book)
            borrow.save()

            book.amount_available -= 1
            book.save()
            if book.amount_available == 0:
                book.is_available = False
                book.save()
    
            return Response(BorrowSerializer(borrow).data, status=status.HTTP_201_CREATED)

@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])      
def return_book(request, pk):
    if request.method == 'POST':
        borrow_book = Borrowed_book.objects.get(user=request.user, pk=pk, returned=False)
        borrow_book.return_date = timezone.now()
        borrow_book.returned = True
        borrow_book.save()

        book = Book.objects.get(pk=pk)
        book.amount_available += 1
        book.save()

        return Response({f'Book returned successfully on {borrow_book.return_date}.'}, status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def review_details(request, pk):
    if request.method == 'GET':
        try:
            review = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({'Error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    if request.method == 'PUT':
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        review = Review.objects.get(pk=pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@permission_classes([IsAuthenticated]) 
@api_view(['POST'])
def review_create(request, pk):
    book = Book.objects.get(pk=pk)
    review_user = request.user

    # Check if the user has already reviewed this watchlist
    review_queryset = Review.objects.filter(book=book, review_user=review_user)
    if review_queryset.exists():
        raise ValidationError("You have made a review already!")

    # Serialize the data
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        # Update the book's ratings
        book.number_rating = book.number_rating + 1

        if book.number_rating == 0:
            book.avg_rating = serializer.validated_data['rating']
        else:
            book.avg_rating = (book.avg_rating + serializer.validated_data['rating']) / book.number_rating
        
        book.save()

        # Save the review
        serializer.save(book=book, review_user=review_user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
