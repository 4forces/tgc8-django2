from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import reverse, get_object_or_404
from .models import Book, Author2
from .forms import BookForm, AuthorForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def home(request):
    return render(request, 'books/home.template.html')


def index(request):
    books = Book.objects.all()
    # passing data as dict to render() function
    return render(request, 'books/index.template.html', {
        'books': books
    })


def view_book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/book_details.template.html', {
        'book': book
    })


def authors(request):
    authors = Author2.objects.all()
    # passing data as dict to render() function
    return render(request, 'books/authors.template.html', {
        'authors': authors
    })


@login_required
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
            messages.success(request,
                             f"New book {form.cleaned_data['title']}"
                             f" has been created")
            return redirect(reverse(index))
    else:
        # create an instance of the BookForm
        create_book_form = BookForm()
        return render(request, 'books/create_book.template.html', {
            'form': create_book_form
        })


def search(request):
    # all_books is a query set that represents ALL the books
    book_query = Book.objects.all()
    search_form = SearchForm()

    # create an empty query  -- represents ALWAYS TRUE
    queries = ~Q(pk__in=[])

    # check if the user has submitted anything
    if request.GET:
        # if the user has filled in the title
        if 'title' in request.GET and request.GET['title']:
            queries = queries & Q(title__icontains=request.GET['title'])

        if 'genre' in request.GET and request.GET['genre']:
            queries = queries & Q(genre=request.GET['genre'])

        if 'tags' in request.GET and request.GET['tags']:
            queries = queries & Q(tags__in=request.GET['tags'])

    # sandbox
    # queries = queries & Q(title__icontains="rings")
    # queries = queries & Q(tags__in=[2])
    # endsanbox

    all_books = book_query.filter(queries)

    return render(request, 'books/search.template.html', {
        'books': all_books,
        'search_form': search_form
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


def update_book(request, book_id):
    # 1. retrieve the book which we are editing,
    # assign it to book_being_updated
    book_being_updated = get_object_or_404(Book, pk=book_id)

    # 2. if the update form is submitted
    if request.method == "POST":

        # create the form and fill in user's data (and assign
        # it to book_form). instance = book_being_updated:
        # specifies this instance is to update an existing model
        book_form = BookForm(request.POST, instance=book_being_updated)
        if book_form.is_valid():
            book_form.save()
            return redirect(reverse(index))
        else:
            return render(request, 'books/update.template.html', {
                "form": book_form,
                # 'book': book_being_updated
            })
    else:
        # if method != POST, create a form with the book details filled in
        book_form = BookForm(instance=book_being_updated)
        return render(request, 'books/update_book.template.html', {
            "form": book_form,
            # 'book': book_being_updated
        })


def edit_author(request, author_id):
    author_to_edit = get_object_or_404(Author2, pk=author_id)

    if request.method == "POST":
        author_form = AuthorForm(request.POST, instance=author_to_edit)
        if author_form.is_valid():
            author_form.save()
            return redirect(reverse(authors))
        else:
            # author_form = AuthorForm(instance=author_to_edit)
            return render(request, 'books/edit_author.template.html', {
                "form": author_form,
                # 'author': author_to_edit
            })
    else:
        author_form = AuthorForm(instance=author_to_edit)
        return render(request, 'books/edit_author.template.html', {
            "form": author_form,
        })


# delete author
def delete_author(request, author_id):
    # this part done when first defining in views.py
    author_to_delete = get_object_or_404(Author2, pk=author_id)
    # this part done later after testing form works
    if request.method == 'POST':
        # use delete() method to remove from database
        author_to_delete.delete()
        return redirect(authors)
    else:
        return render(request, 'books/delete_author.template.html', {
            "author": author_to_delete
        })

# delete book


def delete_book(request, book_id):
    # this part done when first defining in views.py
    book_to_delete = get_object_or_404(Book, pk=book_id)
    # this part done later after testing form works
    if request.method == 'POST':
        # use delete() method to remove from database
        book_to_delete.delete()
        # (index) refers to display_books page
        return redirect(index)
    else:
        return render(request, 'books/delete_book.template.html', {
            "book": book_to_delete
        })
