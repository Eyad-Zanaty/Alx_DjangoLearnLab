from django.contrib import admin
from .models import Book

# Register your models here.
admin.site.register(Book)
class AuthorAdmin(admin.ModelAdmin):
    pass