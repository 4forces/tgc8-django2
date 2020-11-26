from django.shortcuts import render, reverse, HttpResponse, get_object_or_404
from books.models import Book

import stripe

#import settings so that we can access the public stripe key
from django.conf import settings
from django.contrib.sites.models import Site

from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def checkout(request):
    # set the api keys for stripe to work
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # retrieve the shopping cart
    cart = request.session.get('shopping-cart', {})

    line_items = []
    all_book_ids = []

    # go thru each item in the shopping cart
    for book_id, book in cart.items():

        # retrieve the book specified by book_id from our list of books
        book_model = get_object_or_404(Book, pk=book_id)

        # create the line item
        # name, amount, quanity, currency are fixed by stripe
        # you see all the possible properties of a line item at:
        # https://stripe.com/docs/api/invoices/line_item

        item = {
            "name": book_model.title,
            "amount": book_model.cost,
            "quantity": book['qty'],
            "currency": 'usd',
        }

        line_items.append(item)
        all_book_ids.append(str(book_model.id))

    current_site = Site.objects.get_current()
    domain = current_site.domain

    # create a payment session (it's for Stripe)
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],  # take credit cards
        line_items=line_items,
        client_reference_id=request.user.id,
        metadata={
            "all_book_ids": ",".join(all_book_ids)
        },
        mode="payment",
        success_url=domain + reverse('checkout_success'),
        cancel_url=domain + reverse("checkout_cancelled")
    )

    return render(request, "checkout/checkout.template.html", {
        "session_id": session.id,
        "public_key": settings.STRIPE_PUBLISHABLE_KEY
    })


def checkout_success(request):
    return HttpResponse('Payment completed successfully')


def checkout_cancelled(request):
    return HttpResponse('Check out cancelled')

# webhook
@csrf_exempt
def payment_completed(request):
    #1. verify that the data is actually sent by stripe
    endpoint_secret = settings.ENDPOINT_SECRET
    #2. process the order

    # (request.body) = data stripe sends us 
    print(request.body)
    return HttpResponse(status=200)
