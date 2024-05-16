from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    founding_year = models.PositiveIntegerField()
    website = models.URLField()

    def __str__(self):
        return self.name

class Book(models.Model):
    image = models.ImageField(upload_to='book_images/')
    title = models.CharField(max_length=200)
    pages = models.PositiveIntegerField()
    isbn = models.CharField(max_length=20)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    dimensions = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    cover_type = models.CharField(max_length=20, choices=[('Soft', 'Мека'), ('Hard', 'Тврда')])
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50, choices=[('Romance', 'Romance'), ('Thriller', 'Thriller'), ('Biography', 'Biography'), ('Classic', 'Classic'), ('Drama', 'Drama'), ('History', 'History')])

    def __str__(self):
        return self.title