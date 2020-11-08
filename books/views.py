from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Book, Author2
from .forms import BookForm, AuthorForm
# Create your views here.


def index(request):
    books = Book.objects.all()
    # passing data as dict to render() function
    return render(request, 'books/index.template.html', {
        'books': books
    })


def authors(request):
    authors = Author2.objects.all()
    # passing data as dict to render() function
    return render(request, 'books/authors.template.html', {
        'authors': authors
    })


def create_book(request):
    if request.method == "POST":
        # # checks if 'POST' is working
        # return HttpResponse("form submitted")

        # eqv. request.POST is the same request.form in Flask
        # creates the form again, but pass in all user's input
        # that has been submitted
        form = BookForm(request.POST)
        # is_valid() is a django function
        if form.is_valid():
            # save keyed in data to the database
            form.save()
            # eqv. to 'redirect(url_for(index))' in Flask
            return redirect(reverse(index))
    else:
        # create an instance of the BookForm
        create_book_form = BookForm()
        return render(request, 'books/create_book.template.html', {
            'form': create_book_form
        })


def create_author(request):
    if request.method == "POST":
        # # checks if 'POST' is working
        # return HttpResponse("form submitted")
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse(authors))
    else:
        create_author_form = AuthorForm()
        return render(request, 'books/create_author.template.html', {
            'form': create_author_form
        })