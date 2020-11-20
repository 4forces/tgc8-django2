from django import forms
from .models import Book, Author2


# define new class 'BookForm'
class BookForm(forms.ModelForm):
    # meta class to define which model the form is for
    class Meta:
        # define model as 'Book'
        model = Book
        fields = ('title', 'desc', 'ISBN', 'genre', 'category', 'tag')


class AuthorForm(forms.ModelForm):
    class Meta:
        # define model as 'AAuthor2'
        model = Author2
        fields = ('first_name', 'last_name', 'dob')
