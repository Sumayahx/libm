from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=20)
    about = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="book", null=False, default=None)
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    amount_available = models.BigIntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Borrowed_book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} borrowed {self.book.title} on {self.borrow_date}'

class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review')
    description = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book.title + " | " + str(self.review_user) + " | " + str(self.rating)
    

