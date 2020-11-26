from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from books.models import Book

# Create your views here.


def add_to_cart(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    # initialise the shopping cart if it does not exist
    # or fetch the cart if it does
    cart = request.session.get('shopping_cart', {})

    if book_id not in cart:
        book = get_object_or_404(Book, pk=book_id)
        cart[book_id] = {
            'id': book_id,
            'title': book.title,
            'cost': "{:.2f}".format(book.cost/1000),
            'qty': 1
        }
    else:
        # if the shopping cart already has the book,
        # then we assume the user want to buy an additional copy
        cart[book_id]['qty'] += 1

    request.session['shopping_cart'] = cart
    return redirect(reverse('books_route'))


def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    return render(request, 'cart/view_cart.template.html', {
        'cart': cart
    })


def remove_from_cart(request, book_id):
    cart = request.session.get('shopping_cart', {})

    # check if a key in the cart dictionary that matches the book_id
    if book_id in cart:
        del cart[book_id]

        # re-save the session
        request.session['shopping_cart'] = cart
        messages.success(request, "Item successfully removed from the cart")

    return redirect(reverse('books_route'))


def update_quantity(request, book_id):
    # return HttpResponse("Updating quantity of book")
    cart = request.session.get('shopping_cart', {})
    # if the book_iud I want to update the quantity is in the shoppoing cart
    if book_id in cart:
        cart[book_id]['qty'] = request.POST['qty']
        request.session['shopping_cart'] = cart
        messages.success(request, "Quantity has been updated")

    return redirect(reverse('view_cart'))
