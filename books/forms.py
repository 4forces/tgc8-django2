from django import forms
from .models import Book


# define new class 'BookForm'
class BookForm(forms.ModelForm):
    # meta class to define which model the form is for
    class Meta:
        # define model as 'Book'
        model = Book
        fields = ('title', 'desc', 'ISBN')
