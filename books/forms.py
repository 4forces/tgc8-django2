from django import forms
from .models import Book, Author2, Genre, Tag


# define new class 'BookForm'
class BookForm(forms.ModelForm):
    # meta class to define which model the form is for
    class Meta:
        # define model as 'Book'
        model = Book
        fields = ('title', 'desc', 'ISBN', 'genre', 'category', 'tag', 'author', 'owner')


class AuthorForm(forms.ModelForm):
    class Meta:
        # define model as 'AAuthor2'
        model = Author2
        fields = ('first_name', 'last_name', 'dob')


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(), required=False)
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), required =False)