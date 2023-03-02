from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, required=False)
    available = models.BooleanField(required=False)

    def __str__(self):
        return self.title
