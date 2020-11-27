from django.shortcuts import render, reverse, HttpResponse, get_object_or_404
from books.models import Book
from .models import Purchase

import stripe
import json

#import settings so that we can access the public stripe key
from django.conf import settings
from django.contrib.sites.models import Site

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User

# Create your views here.


def checkout(request):
    # set the api keys for stripe to work
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # retrieve the shopping cart
    cart = request.session.get('shopping_cart', {})

    line_items = []
    all_book_ids = []

    # go thru each item in the shopping cart
    for book_id, cart_item in cart.items():

        # retrieve the book specified by book_id from our list of books
        book_model = get_object_or_404(Book, pk=book_id)

        # create the line item
        # name, amount, quanity, currency are fixed by stripe
        # you see all the possible properties of a line item at:
        # https://stripe.com/docs/api/invoices/line_item

        item = {
            "name": book_model.title,
            "amount": book_model.cost,
            "quantity": cart_item['qty'],
            "currency": 'usd',
        }

        line_items.append(item)
        all_book_ids.append({
                'book_id': book_model.id,
                'qty': cart_item['qty']
            })

    current_site = Site.objects.get_current()
    domain = current_site.domain

    # create a payment session (it's for Stripe)
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],  # take credit cards
        line_items=line_items,
        client_reference_id=request.user.id,
        metadata={
            "all_book_ids": json.dumps(all_book_ids)
        },
        mode="payment",
        success_url=domain + reverse("checkout_success"),
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
    # 1. verify that the data is actually sent by stripe
    endpoint_secret = settings.ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        #Invalid payload
        print("Invalid payload")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # signature is invalid
        print("Invalid signature")
        return HttpResponse(status=400)

    # 2. process the order
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        handle_payment(session)

    # (request.body) = data stripe sends us
    print(request.body)
    return HttpResponse(status=200)


def handle_payment(session):
    metadata = session['metadata']
    user = get_object_or_404(User, pk=session['client_reference_id'])
    all_book_ids = json.loads(metadata['all_book_ids'])
    for order_item in all_book_ids:
        book_model = get_object_or_404(Book, pk=order_item['book_id'])
    # print(session)

    # create the purchase model and save it manually
    purchase = Purchase()
    purchase.book = book_model
    purchase.user = user
    purchase.qty = order_item['qty']
    purchase.price = book_model.cost

    # remember to save the model
    purchase.save()

