from django.contrib import admin
from .models import Book, Author, Author2, Genre

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Author2)
admin.site.register(Genre)
admin.site.register(Category)