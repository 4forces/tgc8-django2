from django.shortcuts import render
from books.models import Book

import stripe
from django.conf import settings
from django.contrib.sites.models import sites

# Create your views here.
def checkout(request):
    # set the api keys for stripe to work
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # retrieve the shopping cart
    cart = request.session.get('shopping-cart',{})

    line_items = []
    all_book_ids = []

    for book_id, book in cart.items():

        # retrieve the book specified by book_id
        book = get_object_or_404(Book, pk=book_id)

        # create the line item
        # name, amount, quanity, currency are fixed by stirpe
        item = {
            "name": book_model.title,
            "amount": book_model.cost,
            "quantity": book['qty'],
            "currency": 'usd'
        }

        line_items.append(item)
        all_book_ids.append(str(book_model.id))

    current_site = Site.objects

    # create a payment session (it's for Stripe)
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],  # take credit cards
        line_items=line_items,
        client_reference_id=request.user.id,
        metadata={
            "all_book_ids": ",".join(all_book_ids)
        },
        mode="payment",
        success_url = domain + reverse('checkout_success'),
        cancel_url=domain + reverse("checkout_cancelled")
    )