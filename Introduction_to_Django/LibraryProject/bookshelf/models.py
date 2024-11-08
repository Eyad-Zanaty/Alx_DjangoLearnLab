from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length= 200)
    author = models.CharField(max_length= 100)
    publication_year = models.IntegerField()

book01 = Book(title='1984', author='George Orwell', publication_year= 1949)
books = Book.objects.all()
book02 = Book.objects.get(title="1984")
book02.title = "Nineteen Eighty-Four"
book02.save()
book02.delete()