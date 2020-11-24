def cart_contents(request):
    cart = request.session.get('shopping-cart',{})
    return {
        'shopping_cart': cart,
        'number_of_items': len(cart)
    }